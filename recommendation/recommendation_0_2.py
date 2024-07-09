from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    TemporalIndicatorCombination,
)
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod

from digipod.criterion.postop_patients import PostOperativePatientsUntilDay6
from digipod.criterion.preop_patients import InpatientPatients, IntensiveCarePatients
from digipod.criterion.scores import *
from digipod.recommendation import package_version

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
p_morning_normalward = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDayMorningShift_NormalWard",
    url="",
    base_criterion=base_criterion,
    population=LogicalCriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        InpatientPatients(),
        category=CohortCategory.POPULATION,
    ),
    intervention=TemporalIndicatorCombination.Day(
        TemporalIndicatorCombination.MorningShift(
            LogicalCriterionCombination.Or(
                TDCAM_documented,  # 3DCAM Morning
                AT4_documented,  # AT4 Morning
                CAM_documented,  # CAM Morning
                DRS_documented,  # DRS Morning
                DOS_documented,  # DOS Morning
                NUDESC_documented,  # NuDESC Morning
                category=CohortCategory.INTERVENTION,
            ),
            category=CohortCategory.INTERVENTION,
        ),
        category=CohortCategory.INTERVENTION,
    ),
)


p_morning_icu = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDayMorningShift_ICU",
    url="",
    base_criterion=base_criterion,
    population=LogicalCriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        IntensiveCarePatients(),
        category=CohortCategory.POPULATION,
    ),
    intervention=TemporalIndicatorCombination.Day(
        TemporalIndicatorCombination.MorningShift(
            LogicalCriterionCombination.Or(
                ###########################################
                # WARNING: THESE ARE WRONG, REMOVE THEM
                TDCAM_documented,  # 3DCAM Morning
                AT4_documented,  # AT4 Morning
                CAM_documented,  # CAM Morning
                ###########################################
                # CAMICU Morning
                # DDS Morning
                # ICDSC Morning
                category=CohortCategory.INTERVENTION,
            ),
            category=CohortCategory.INTERVENTION,
        ),
        category=CohortCategory.INTERVENTION,
    ),
)


#############################
# Recommendation collections
#############################
rec_0_2_Delirium_Screening = Recommendation(
    pi_pairs=[p_morning_normalward, p_morning_icu],
    base_criterion=base_criterion,
    name="Recommendation0_2PostOperativeScreeningOfDelirium",
    title="Recommendation 0.2: Postoperative screening of delirium",
    url="",
    version="0.1",
    description="Delirium should be screened at least once per day (preferably two or three times per day) for at least 3 days, starting in the recovery room or in the PACU on the day of surgery or latest on postoperative day 1.",
    package_version=package_version,
)
