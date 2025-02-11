from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod

from digipod.criterion.preop_patients import (
    adultPatientsPreoperativelyGeneralOnSurgeryDayAndBefore,
)
from digipod.criterion.scores import (
    AT4_documented,
    CAM_documented,
    DOS_documented,
    DRS_documented,
    NUDESC_documented,
    TDCAM_documented,
)
from digipod.recommendation import package_version
from digipod.recommendation.util import AnyTime

base_criterion = PatientsActiveDuringPeriod()

_RecPlanPreoperativeDeliriumScreening = PopulationInterventionPair(
    name="",
    url="",
    base_criterion=base_criterion,
    population=adultPatientsPreoperativelyGeneralOnSurgeryDayAndBefore,
    intervention=AnyTime(
        LogicalCriterionCombination.AtLeast(
            NUDESC_documented,
            DRS_documented,
            DOS_documented,
            CAM_documented,
            AT4_documented,
            TDCAM_documented,
            threshold=1,
            category=CohortCategory.INTERVENTION,
        )
    ),
)

rec_0_1_Delirium_Screening = Recommendation(
    pi_pairs=[_RecPlanPreoperativeDeliriumScreening],
    base_criterion=base_criterion,
    name="Rec 0.1: PreoperativeDeliriumScreening",
    title="Recommendation 0.1: Preoperative Screening of Delirium",
    url="",
    version="0.2.0",
    description="Adult patients before undergoing a surgical intervention of any type independently of the type of "
    "anesthesia, on the day of the surgical intervention or maximum 42 days before: "
    "Perform baseline delirium screening.",
    package_version=package_version,
)
