from typing import List

from execution_engine.constants import CohortCategory
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.abstract import (
    Criterion,
    column_interval_type,
    observation_end_datetime,
    observation_start_datetime,
)
from execution_engine.omop.criterion.combination.combination import CriterionCombination
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    FixedWindowTemporalIndicatorCombination,
    TemporalIndicatorCombination,
)
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.criterion.continuous import ContinuousCriterion
from execution_engine.omop.criterion.drug_exposure import DrugExposure
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.util.interval import IntervalType
from execution_engine.util.value import Value, ValueConcept, ValueNumber
from sqlalchemy import select
from sqlalchemy.sql import Select

from digipod import concepts
from digipod.concepts import (
    Baseline_Bradycardia,
    Bradycardia_During_Surgery,
    Drug_Induced_Bradycardia,
    Drug_Induced_Hypotension,
    Hypotension_During_Surgery,
    Low_Blood_Pressure,
)
from digipod.criterion.intraop_patients import IntraOperativePatients
from digipod.criterion.patients import AdultPatients, FirstDexmedetomidineAdministration
from digipod.criterion.postop_patients import IntraOrPostOperativePatients
from digipod.criterion.preop_patients import PreOperativePatientsBeforeSurgery
from digipod.criterion.scores import score_threshold

ValuePositive = ValueConcept(value=concepts.Positive)

ValueNotPerformed = ValueConcept(value=concepts.NotPerformed)


def score_criterion(
    concept: Concept,
    value: None | Value,
    category: CohortCategory = CohortCategory.POPULATION,
) -> LogicalCriterionCombination:
    """
    Return NOT(concept = value) OR NOT(positive) OR not_performed for the given concept
    """
    if value is None:
        return LogicalCriterionCombination.Or(
            LogicalCriterionCombination.Not(score_threshold(concept, ValuePositive)),
            score_threshold(concept, ValueNotPerformed),
        )
    else:
        return LogicalCriterionCombination.Or(
            LogicalCriterionCombination.Not(score_threshold(concept, value)),
            LogicalCriterionCombination.Not(score_threshold(concept, ValuePositive)),
            score_threshold(concept, ValueNotPerformed),
        )


NuDESC_negative = score_criterion(
    concepts.NuDESC, ValueNumber.parse(">=2", unit=concepts.unit_score)
)  # we only support >=, hence we must use >=2 instead of >1
ICDSC_negative = score_criterion(
    concepts.ICDSC, ValueNumber.parse(">=4", unit=concepts.unit_score)
)
CAM_negative = score_criterion(concepts.CAM, value=None)
DRS_negative = score_criterion(
    concepts.DRS, ValueNumber.parse(">=12", unit=concepts.unit_score)
)
DOS_negative = score_criterion(
    concepts.DOS, ValueNumber.parse(">=3", unit=concepts.unit_score)
)
TDCAM_negative = score_criterion(concepts.TDCAM, value=None)
CAM_ICU_negative = score_criterion(concepts.CAM_ICU, value=None)
DDS_negative = score_criterion(
    concepts.DDS, ValueNumber.parse(">=8", unit=concepts.unit_score)
)
FourAT_negative = score_criterion(
    concepts.FourAT, ValueNumber.parse(">=4", unit=concepts.unit_score)
)

dementia = ContinuousCriterion(concept=concepts.Dementia)

deliriumAssessmentPerformed = ContinuousCriterion(
    concept=concepts.AssessmentOfDelirium,
)

riskAssessmentPerformed = PointInTimeCriterion(
    concept=concepts.RiskAssessmentDone,
    forward_fill=True,
)

drugDexmedetomidine = DrugExposure(
    ingredient_concept=concepts.Dexmedetomidine,
    dose=None,
    route=None,
)


# Before Dexmedetomidine started
baselineBradycardia = ConditionOccurrence(concept=Baseline_Bradycardia)

lowBloodPressure = ConditionOccurrence(concept=Low_Blood_Pressure)

# After Dexmedetomidine started
drugInducedBradycardia = ConditionOccurrence(concept=Drug_Induced_Bradycardia)

drugInducedHypotension = ConditionOccurrence(concept=Drug_Induced_Hypotension)

# During surgery
bradycardiaDuringSurgery = ConditionOccurrence(concept=Bradycardia_During_Surgery)

hypotensionDuringSurgery = ConditionOccurrence(concept=Hypotension_During_Surgery)


"""
Before Surgery:
- >= 18 years
- NO Dementia ($sct#404684003 "Clinical finding (finding)")
- Assessment of delirium performed $sct#733870009 "Assessment of delirium (procedure)"
- Assessment of risk performed $sct#712741005 "Risk assessment done (situation)"
- in the following scores:
    POSITIVE = $sct#10828004 "Positive (qualifier value)"
    NOT PERFORMED = $sct#262008008 "Not performed (qualifier value)"
- NuDesc
    - NOT(>1) OR NOT(POSITIVE) OR "Not Performed"
- ICDSC
    - NOT(>= 4) OR NOT(POSITIVE) OR "Not Performed"
- CAM
    - NOT(POSITIVE) OR "Not Performed"
- DRS
    - NOT(>= 12) OR NOT(POSITIVE) OR "Not Performed"
- DOS
    - NOT(>= 3) OR NOT(POSITIVE) OR "Not Performed"
- 3DCAM
    - NOT(POSITIVE) OR "Not Performed"
- CAM-ICU
    - NOT(POSITIVE) OR "Not Performed"
- DDS
    - NOT >=8 OR NOT(POSITIVE) OR "Not Performed"
- 4 AT
    - NOT >= 4 OR NOT(POSITIVE) OR "Not Performed"

During or after surgery:
- Administration of Dexmedetomidine $sct#437750002 "Dexmedetomidine (substance)"
"""
basePopulationPreOp = LogicalCriterionCombination.And(
    PreOperativePatientsBeforeSurgery(),  # gibt einen zeitraum aus, ist gut
    AdultPatients(),
)

basePopulationIntraPost = LogicalCriterionCombination.And(
    IntraOrPostOperativePatients(),  # gibt einen zeitraum aus, ist gut
    AdultPatients(),
)


def temporal_filter_criteria(
    criteria: List[Criterion | CriterionCombination],
    filter_: Criterion | CriterionCombination,
    category: CohortCategory = CohortCategory.POPULATION,
) -> list[TemporalIndicatorCombination]:
    """
    Filters each criterion in criteria individually and then returns an "AnyTime" TemporalCombination,
    meaning a single interval spanning the whole observed time, either POSITIVE if there is any
    POSITIVE criterion after filtering, otherwise negative
    """
    return [
        FixedWindowTemporalIndicatorCombination.AnyTime(
            LogicalCriterionCombination.And(c, filter_),
        )
        for c in criteria
    ]


popAdultPatWithoutDementiaGettingDexmedetomidineIntraOrPostOP = (
    LogicalCriterionCombination.And(
        FixedWindowTemporalIndicatorCombination.AnyTime(
            LogicalCriterionCombination.And(
                basePopulationPreOp,
                *temporal_filter_criteria(
                    [
                        LogicalCriterionCombination.Not(
                            dementia,
                        ),  # nur ab beginn -> braucht umfassung
                        deliriumAssessmentPerformed,
                        riskAssessmentPerformed,
                        NuDESC_negative,
                        ICDSC_negative,
                        CAM_negative,
                        DRS_negative,
                        DOS_negative,
                        TDCAM_negative,
                        CAM_ICU_negative,
                        DDS_negative,
                        FourAT_negative,
                    ],
                    basePopulationPreOp,
                ),
            ),
        ),
        LogicalCriterionCombination.And(
            IntraOrPostOperativePatients(),
            drugDexmedetomidine,
        ),
    )
)

"""
Before surgery
- >= 18 Jahre
- WITH dementia

During or after surgery:
- Administration of Dexmedetomidine $sct#437750002 "Dexmedetomidine (substance)"
"""
popAdultPatWithDementiaGettingDexmedetomidineIntraOrPostOP = (
    LogicalCriterionCombination.And(
        FixedWindowTemporalIndicatorCombination.AnyTime(
            LogicalCriterionCombination.And(
                basePopulationPreOp,
                *temporal_filter_criteria([dementia], basePopulationPreOp),
            ),
        ),
        LogicalCriterionCombination.And(
            IntraOrPostOperativePatients(),
            drugDexmedetomidine,
        ),
    )
)


"""
During or After Surgery
- Age > 18
- Dexmedetomidine
- $sct#182929008 "Administration of prophylactic drug or medicament (procedure)"

Before Dexmedetomidine started:
- $sct#278085001 "Baseline bradycardia (finding)"
- $sct#45007003 "Low blood pressure (disorder)"

After Dexmedetomidine started:
- $sct#397841007 "Drug-induced bradycardia (disorder)"
- $sct#234171009 "Drug-induced hypotension (disorder)"

During surgery
- $cs-digipod#031 "Bradycardia during surgery"
- $sct#10901000087102 "Hypotension during surgery (disorder)"
"""


class PatientsBeforeFirstDexAdministration(FirstDexmedetomidineAdministration):
    """
    Select patients in the timeframe before the first Dexmedetomidine administration.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for the time period before Dexmedetomidine administration.
        """

        subquery = self._query_first_dexmedetomidine()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            observation_start_datetime.label("interval_start"),
            subquery.c.drug_exposure_start_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first administration per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query


class PatientsAfterFirstDexAdministration(FirstDexmedetomidineAdministration):
    """
    Select patients in the timeframe after the first Dexmedetomidine administration.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for the time period after Dexmedetomidine administration.
        """

        subquery = self._query_first_dexmedetomidine()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            subquery.c.drug_exposure_start_datetime.label("interval_start"),
            observation_end_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first administration per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query


condBeforeOrAfter = LogicalCriterionCombination.And(
    *temporal_filter_criteria([drugDexmedetomidine], filter_=basePopulationIntraPost),
    basePopulationIntraPost,
)


intraOp = IntraOperativePatients()
beforeDexmedetomidine = PatientsBeforeFirstDexAdministration()
afterDexmedetomidine = PatientsAfterFirstDexAdministration()

condBeforeDex = temporal_filter_criteria(
    [baselineBradycardia, lowBloodPressure], filter_=beforeDexmedetomidine
)
condAfterDex = temporal_filter_criteria(
    [drugInducedBradycardia, drugInducedHypotension], filter_=afterDexmedetomidine
)
condIntraOp = LogicalCriterionCombination.And(
    *temporal_filter_criteria(
        [bradycardiaDuringSurgery, hypotensionDuringSurgery], filter_=intraOp
    ),
)

popAdultPatientsIntraOrPostOPWithDexmedetomidineAndBradyOrHypo = (
    LogicalCriterionCombination.And(
        condBeforeOrAfter,
        *condBeforeDex,
        *condAfterDex,
        condIntraOp,
    )
)
