from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.logic import *
from execution_engine.util.temporal_logic_util import AnyTime

from digipod.criterion.assessments import *
from digipod.criterion.non_pharma_measures import (
    PreOperativeBeforeDayOfSurgery,
)
from digipod.criterion.patients import AgeLimitPatient

recommendation = Recommendation(
    expr=
        PopulationInterventionPairExpr(
            population_expr=And(
                AgeLimitPatient(min_age_years=70),
                PreOperativeBeforeDayOfSurgery(assessmentForRiskOfPostOperativeDelirium),
            ),
            intervention_expr=MinCount(
                    AnyTime(healthcareInformationExchange),
                And(AnyTime(multidisciplinaryCareConference), AnyTime(multidisciplinaryCaseManagement)),
                threshold=1
            ),
            name="RecPlanExchangeHealthcareInformation",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanExchangeHealthcareInformation",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollShareRFOfOlderAdultsPreOPAndRegisterPreventiveStrategies",
    title="Recommendation Collection: Share the results of the screening for POD risk factors among the care team and discuss and register the preventive strategies in the medical records in 'Older Adult Surgical Patients After Preoperative Screening of Risk Factors for POD'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollShareRFOfOlderAdultsPreOPAndRegisterPreventiveStrategies",
    version="0.2.0",
    description="Recommendation collection for older adult patients that were screened for risk factors for postoperative delirium before undergoing a surgical intervention of any type independently of the type of anesthesia: Share the results of the screening for POD risk factors among the care team and discuss and register the preventive strategies in the medical records.",
    package_version="latest",
)
