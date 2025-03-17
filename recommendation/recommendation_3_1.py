from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.noop import NoopCriterion
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.logic import *

from digipod.criterion.patients import AgeLimitPatient
from digipod.criterion.preop_patients import PreOperativePatientsBeforeEndOfSurgery

recommendation = Recommendation(
    expr=PopulationInterventionPairExpr(
        population_expr=TemporalMinCount(
            AgeLimitPatient(min_age_years=18),
            PreOperativePatientsBeforeEndOfSurgery(),
            threshold=1,
            start_time=None,
            end_time=None,
            interval_type=None,
            interval_criterion=PreOperativePatientsBeforeEndOfSurgery(),
        ),
        intervention_expr=MinCount(Not(NoopCriterion()), NoopCriterion(), threshold=1),
        name="RecPlanNoSpecProphylacticDrugForPODAndShowRecommendation",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanNoSpecProphylacticDrugForPODAndShowRecommendation",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollAdultSurgicalPatNoSpecProphylacticDrugForPOD",
    title="Recommendation Collection: Do not suggest the use of any drug as a prophylactic measure to reduce the incidence of POD in 'General Adult Surgical Patients Pre- and Intraoperatively'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollAdultSurgicalPatNoSpecProphylacticDrugForPOD",
    version="0.2.0",
    description="Recommendation collection for adult patients before and/or during a surgical intervention of any type independently of the type of anesthesia: Do not administrate or suggest the use of any drug as a prophylactic measure to reduce the incidence of postoperative delirium (POD).",
    package_version="latest",
)
