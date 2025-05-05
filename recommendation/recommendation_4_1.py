from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.task.process import IntervalWithCount, interval_like
from execution_engine.task.task import Task
from execution_engine.util import logic
from execution_engine.util.interval import IntervalType
from execution_engine.util.logic import *
from execution_engine.util.temporal_logic_util import AnyTime
from execution_engine.util.types import PersonIntervals

from digipod.criterion.assessments import *
from digipod.criterion.non_pharma_measures import (
    PreOperativeUntilTwoHoursBeforeDayOfSurgery,
)
from digipod.criterion.patients import AgeLimitPatient

_piScreeningOfRFInOlderPatientsPreOP = PopulationInterventionPairExpr(
            population_expr=PreOperativeUntilTwoHoursBeforeDayOfSurgery(
                AgeLimitPatient(min_age_years=70),
            ),
            intervention_expr=MinCount(
                AnyTime(assessmentForRiskOfPostOperativeDelirium),
                And(
                    And(
                        cardiacAssessment,
                        neurologicalAssessment,
                        cardiovascularEvaluation,
                        diabetesScreening,
                        anemiaScreening,
                        depressedMoodAssessment,
                        painAssessment,
                        anxietyAssessment,
                        cognitiveFunctionAssessment,
                        dementiaAssessment,
                        frailtyAssessment,
                        sensoryImpairmentAssessment,
                        nutritionalAssessment,
                        medicationAdministrationAssessment,
                        electrolytesMeasurement,
                        swallowingFunctionEvaluation,
                        anticholinergicBurdenScale,
                    ),
                    Or(
                        preAnestheticAssessment,
                        dehydrationRiskAssessment,
                        impairedNutritionRiskAssessment,
                        hypovolemiaRiskAssessment,
                    ),
                ),
                threshold=1,
            ),
            name="RecPlanScreeningOfRFInOlderPatientsPreOP",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanScreeningOfRFInOlderPatientsPreOP",
            base_criterion=PatientsActiveDuringPeriod(),
        )

_piOptimizationOfPreOPStatusInOlderPatPreoperatively = PopulationInterventionPairExpr(
            population_expr=And(
                PreOperativeUntilTwoHoursBeforeDayOfSurgery(
                    AgeLimitPatient(min_age_years=70),
                ),
                PreOperativeUntilTwoHoursBeforeDayOfSurgery(
                    assessmentForRiskOfPostOperativeDelirium,
                ),
                PreOperativeUntilTwoHoursBeforeDayOfSurgery(
                    optimizablePreopRiskFactorPresent,
                ),
            ),
            intervention_expr=MinCount(AnyTime(preoperativeRiskFactorOptimization), threshold=1),
            name="RecPlanOptimizationOfPreOPStatusInOlderPatPreoperatively",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanOptimizationOfPreOPStatusInOlderPatPreoperatively",
            base_criterion=PatientsActiveDuringPeriod(),
        )


class CombineRecommendation4_1(logic.And):
    """
    Combines the two distinct population/intervention pairs in this recommendation and calculates
    a weighted sum of the counts.
    """

    @staticmethod
    def prepare_data(task: Task, data: list[PersonIntervals]) -> list[PersonIntervals]:
        """
        Selects and returns the PersonIntervals in the order
        - result of _piScreeningOfRFInOlderPatientsPreOP
        - result of _piOptimizationOfPreOPStatusInOlderPatPreoperatively

        This function is used in task.Task to sort the incoming data such that the `count_intervals` function
        can rely on this order.
        """
        assert task.expr.args[0].name == _piScreeningOfRFInOlderPatientsPreOP.name
        assert task.expr.args[1].name == _piOptimizationOfPreOPStatusInOlderPatPreoperatively.name

        idx_risk_screening = task.get_predecessor_data_index(task.expr.args[0])
        idx_risk_optimization = task.get_predecessor_data_index(task.expr.args[1])

        if len(data) != 2:
            raise ValueError('Expected exactly 2 inputs')

        return [data[idx_risk_screening], data[idx_risk_optimization]]


    @staticmethod
    def count_intervals(start: int, end: int, intervals: list[IntervalWithCount]
    ) -> IntervalWithCount:
        """
        Combines two intervals into a single IntervalWithCount, handling special cases.

        This function is used as a callback in `process.find_rectangles`.

        Due to ` prepare_data`, the intervals are expected to be (in that order):
        - index 0: result of _piScreeningOfRFInOlderPatientsPreOP
        - index 1: result of _piOptimizationOfPreOPStatusInOlderPatPreoperatively

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
        result_type = left_type & right_type
        right_count = (1 if right_type == IntervalType.POSITIVE else 0)
        left_count = (1 if left_type == IntervalType.POSITIVE else 0)
        result_count = (left_count + right_count) / 2

        return IntervalWithCount(start, end, result_type, result_count)


recommendation = Recommendation(
    expr=CombineRecommendation4_1(_piScreeningOfRFInOlderPatientsPreOP
        , _piOptimizationOfPreOPStatusInOlderPatPreoperatively
    ),
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollPreoperativeRFAssessmentAndOptimization",
    title="Recommendation Collection: Assess risk factors for postoperative delirium and address patient's needs to optimize the preoperative status in 'Older Adult Surgical Patients Preoperatively' & 'Older Adult Surgical Patients With Optimizable Risk Factors Identified Preoperatively'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollPreoperativeRFAssessmentAndOptimization",
    version="0.3.0",
    description="Recommendation collection for older adult patients before undergoing a surgical intervention of any type independently of the type of anesthesia: Assess risk factors for postoperative delirium (POD) and address patient's needs to optimize the preoperative status",
    package_version="latest",
)
