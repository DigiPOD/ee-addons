from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.omop.vocabulary import LOINC, SNOMEDCT, standard_vocabulary
from execution_engine.task.process import IntervalWithCount, interval_like
from execution_engine.task.task import Task
from execution_engine.util import logic, temporal_logic_util
from execution_engine.util.interval import IntervalType
from execution_engine.util.types import PersonIntervals

from digipod.criterion import AgeDocumented
from digipod.criterion.preop_patients import (
    preOperativeAdultBeforeDayOfSurgeryPatients,
    preOperativeAdultBeforeDayOfSurgeryPatientsMMSElt3,
)
from digipod.recommendation import package_version
from digipod.terminology import vocabulary

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

ageDocumented = AgeDocumented()

# $sct#302132005 "American Society of Anesthesiologists physical status class (observable entity)"
asaDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(SNOMEDCT.system_uri, "302132005"),
    value_required=False,
)

#  $cs-digipod#009 "Result of Charlson Comorbidity Index"
cciDocumented = PointInTimeCriterion(
    concept=vocabulary.RESULT_OF_CHARLSON_COMORBIDITY_INDEX,
    value_required=False,
)

#  $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
miniCogDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "713408000", standard=False
    ),  # $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
    value_required=False,
)

# $loinc#72172-0 "Total score [MoCA]"
mocaDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        LOINC.system_uri, "72172-0"
    ),  # #72172-0 "Total score [MoCA]"
    value_required=False,
)

# $sct-uk#711061000000109 "Addenbrooke's cognitive examination revised - score (observable entity)"
acerDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "711061000000109", standard=False
    ),  # $sct-uk#711061000000109 "Addenbrooke's cognitive examination revised - score (observable entity)"
    value_required=False,
)

# $sct#447316007 "Mini-mental state examination score (observable entity)"
mmseDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "447316007", standard=False
    ),  # $sct#447316007 "Mini-mental state examination score (observable entity)"
    value_required=False,
)


#############
# PI Pairs
#############

_RecPlanCheckRiskFactorsAgeASACCIMiniCog = PopulationInterventionPairExpr(
    name="RecPlanCheckRiskFactorsAgeASACCIMiniCog",
    url="",
    base_criterion=base_criterion,
    population_expr=preOperativeAdultBeforeDayOfSurgeryPatients,
    intervention_expr=logic.MinCount(
        temporal_logic_util.AnyTime(ageDocumented),
        temporal_logic_util.AnyTime(asaDocumented),
        temporal_logic_util.AnyTime(cciDocumented),
        temporal_logic_util.AnyTime(miniCogDocumented),
        threshold=4
    ),
)

_RecPlanCheckRiskFactorsMoCAACERMMSE = PopulationInterventionPairExpr(
    name="RecPlanCheckRiskFactorsMoCAACERMMSE",
    url="",
    base_criterion=base_criterion,
    population_expr=preOperativeAdultBeforeDayOfSurgeryPatientsMMSElt3,
    intervention_expr=logic.MinCount(
        temporal_logic_util.AnyTime(mocaDocumented),
        temporal_logic_util.AnyTime(acerDocumented),
        temporal_logic_util.AnyTime(mmseDocumented),
        threshold=1,
    ),
)

class CombineRecommendation2_1(logic.Or):
    """
    Combines the two distinct population/intervention pairs in this recommendation and calculates
    a weighted sum of the counts.
    """

    @staticmethod
    def prepare_data(task: Task, data: list[PersonIntervals]) -> list[PersonIntervals]:
        """
        Selects and returns the PersonIntervals in the order
        - result of _RecPlanCheckRiskFactorsAgeASACCIMiniCog
        - result of _RecPlanCheckRiskFactorsMoCAACERMMSE

        This function is used in task.Task to sort the incoming data such that the `count_intervals` function
        can rely on this order.
        """
        assert task.expr.args[0].name == _RecPlanCheckRiskFactorsAgeASACCIMiniCog.name
        assert task.expr.args[1].name == _RecPlanCheckRiskFactorsMoCAACERMMSE.name

        idx_check_risk_factors = task.get_predecessor_data_index(task.expr.args[0])
        idx_mmse = task.get_predecessor_data_index(task.expr.args[1])

        if len(data) != 2:
            raise ValueError('Expected exactly 2 inputs')

        return [data[idx_check_risk_factors], data[idx_mmse]]


    @staticmethod
    def count_intervals(start: int, end: int, intervals: list[IntervalWithCount]
    ) -> IntervalWithCount:
        """
        Combines two intervals into a single IntervalWithCount, handling special cases.

        This function is used as a callback in `process.find_rectangles`.

        Due to ` prepare_data`, the intervals are expected to be (in that order):
        - index 0: result of _RecPlanCheckRiskFactorsAgeASACCIMiniCog
        - index 1: result of _RecPlanCheckRiskFactorsMoCAACERMMSE

        If the second interval is NOT_APPLICABLE - i.e. the patient is not part of the population of the second
        PI pair, the first interval is returned directly.
        Otherwise, a union of both intervals is created, and the count value is
        calculated based on the notion that there are 4 items to be fulfilled in
        _RecPlanCheckRiskFactorsAgeASACCIMiniCog, and 1 item in _RecPlanCheckRiskFactorsMoCAACERMMSE.
        Accordingly, a weighted count is calculated.
        """
        left, right = intervals

        # we need to take special care, unfortunately, that:
        # - left or right can be None (equivalent to NEGATIVE interval)
        # - left and right be with or without count (if without, .count is the namedtuple build-in method)

        left_type = left.type if left is not None else IntervalType.NEGATIVE
        right_type = right.type if right is not None else IntervalType.NEGATIVE

        if right_type is IntervalType.NOT_APPLICABLE:
            # the second PI Pair is not applicable, so we just return the count of #1
            return interval_like(left, start, end)

        # otherwise, we return the union of both intervals
        result_type = left_type | right_type
        right_count = (1 if right_type == IntervalType.POSITIVE else 0)
        left_count = left.count if left is not None and left.type is not IntervalType.NOT_APPLICABLE else 0
        result_count = (4 * left_count + right_count) / 5

        return IntervalWithCount(start, end, result_type, result_count)

#############################
# Recommendation collections
#############################
RecCollCheckRFAdultSurgicalPatientsPreoperatively = Recommendation(
    expr=CombineRecommendation2_1(
        _RecPlanCheckRiskFactorsAgeASACCIMiniCog,
        _RecPlanCheckRiskFactorsMoCAACERMMSE,
    ),
    base_criterion=base_criterion,
    name="Rec 2.1: CheckRFAdultSurgicalPatientsPreoperatively",
    title="Recommendation 2.1: Check risk factors in 'General Adult Surgical Patients' Preoperatively",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollCheckRFAdultSurgicalPatientsPreoperatively",
    version="0.2.0",
    description="Adult patients before undergoing a surgical intervention of any type independently of the type of anesthesia: "
    "Check risk factors age, American Society of Anesthesiology Physical status score (ASA), "
    "Charlson Comorbidity Index (CCI) and Mini-cog test score (Mini-cog). "
    "If Mini-cog test score is equal to or higher than 3, perform Montreal Cognitive Assessment (MoCA), A"
    "ddenbrooke's Cognitive Examination (ACE-R) or Mini Mental State Examination (MMSE). "
    "Please note that MMSE is not free of charge (license fees)",
    package_version=package_version,
)
