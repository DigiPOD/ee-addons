from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util import logic, temporal_logic_util

from digipod.criterion.preop_patients import (
    adultPatientsPreoperativelyOnSurgeryDayAndBefore,
)
from digipod.recommendation import package_version
from digipod.recommendation.recommendation_0_2 import icu_scores, normalward_scores

base_criterion = PatientsActiveDuringPeriod()

_RecPlanPreoperativeDeliriumScreening = PopulationInterventionPairExpr(
    name="",
    url="",
    base_criterion=base_criterion,
    population_expr=adultPatientsPreoperativelyOnSurgeryDayAndBefore,
    intervention_expr=
        logic.MinCount(
            temporal_logic_util.AnyTime(logic.Or(
                normalward_scores, icu_scores
            )),
            threshold=1,
        )
)



rec_0_1_Delirium_Screening = Recommendation(
    expr=_RecPlanPreoperativeDeliriumScreening,
    base_criterion=base_criterion,
    name="Rec 0.1: PreoperativeDeliriumScreening",
    title="Recommendation 0.1: Preoperative Screening of Delirium",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollPreoperativeDeliriumScreening",
    version="0.2.0",
    description="Adult patients before undergoing a surgical intervention of any type independently of the type of "
    "anesthesia, on the day of the surgical intervention or maximum 42 days before: "
    "Perform baseline delirium screening.",
    package_version=package_version,
)
