from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod

from digipod.criterion.patients import AdultPatients
from digipod.criterion.postop_patients import PostOperativePatientsUntilDay6
from digipod.criterion.preop_patients import InpatientPatients, IntensiveCarePatients
from digipod.criterion.scores import *
from digipod.recommendation import package_version
from digipod.recommendation.util import (
    AfternoonShift,
    AtLeast,
    Day,
    MorningShift,
    NightShift,
)

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

#############
# Day0
#############

#############
# PI Pairs
#############


normalward_scores = LogicalCriterionCombination.Or(
    TDCAM_documented,  # 3DCAM Morning
    AT4_documented,  # AT4 Morning
    CAM_documented,  # CAM Morning
    DRS_documented,  # DRS Morning
    DOS_documented,  # DOS Morning
    NUDESC_documented,  # NuDESC Morning
    category=CohortCategory.INTERVENTION,
)

icu_scores = LogicalCriterionCombination.Or(
    CAMICU_documented,  # 3DCAM Morning
    DDS_documented,  # AT4 Morning
    ICDSC_documented,  # CAM Morning
    category=CohortCategory.INTERVENTION,
)

pi_normalward = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDay_NormalWard",
    url="",
    base_criterion=base_criterion,
    population=LogicalCriterionCombination.And(
        AdultPatients(),
        PostOperativePatientsUntilDay6(),
        InpatientPatients(),
        category=CohortCategory.POPULATION,
    ),
    intervention=AtLeast(
        Day(MorningShift(normalward_scores)),
        Day(AfternoonShift(normalward_scores)),
        Day(NightShift(normalward_scores)),
        threshold=2,
    ),
)


pi_icu = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDay_ICU",
    url="",
    base_criterion=base_criterion,
    population=LogicalCriterionCombination.And(
        AdultPatients(),
        PostOperativePatientsUntilDay6(),
        IntensiveCarePatients(),
        category=CohortCategory.POPULATION,
    ),
    intervention=AtLeast(
        Day(MorningShift(icu_scores)),
        Day(AfternoonShift(icu_scores)),
        Day(NightShift(icu_scores)),
        threshold=2,
    ),
)


#############################
# Recommendation collections
#############################
rec_0_2_Delirium_Screening = Recommendation(
    pi_pairs=[pi_normalward, pi_icu],
    base_criterion=base_criterion,
    name="Rec 0.2: PostOperativeScreeningOfDelirium",
    title="Recommendation 0.2: Postoperative screening of delirium",
    url="",
    version="0.1",
    description="Delirium should be screened at least once per day (preferably two or three times per day) for at least 3 days, starting in the recovery room or in the PACU on the day of surgery or latest on postoperative day 1.",
    package_version=package_version,
)
