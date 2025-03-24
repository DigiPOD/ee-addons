from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.logic import *
from execution_engine.util.types import Timing

from digipod.criterion.patients import AgeLimitPatient

recommendation = Recommendation(
  expr=Or(
  PopulationInterventionPairExpr(
      population_expr=And(
          AgeLimitPatient(
              min_age_years=70
            ),
          ProcedureOccurrence(
              static=False,
              timing=None,
              concept=Concept(concept_id=4301351, concept_name='Surgical procedure', concept_code='387713003', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
              value=None
            ),
          ProcedureOccurrence(
              static=False,
              timing=None,
              concept=Concept(concept_id=2000000017, concept_name='Assessment for risk of post-operative delirium', concept_code='017', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
              value=None
            )
        ),
      intervention_expr=Observation(
          static=False,
          value_required=False,
          concept=Concept(concept_id=4296383, concept_name='Healthcare information exchange', concept_code='386317007', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
          forward_fill=True,
          value=None,
          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None)
        ),
      name='RecPlanExchangeHealthcareInformation',
      url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanExchangeHealthcareInformation',
      base_criterion=PatientsActiveDuringPeriod()
    ),
  PopulationInterventionPairExpr(
      population_expr=And(
          AgeLimitPatient(
              min_age_years=70
            ),
          ProcedureOccurrence(
              static=False,
              timing=None,
              concept=Concept(concept_id=4301351, concept_name='Surgical procedure', concept_code='387713003', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
              value=None
            ),
          ProcedureOccurrence(
              static=False,
              timing=None,
              concept=Concept(concept_id=2000000017, concept_name='Assessment for risk of post-operative delirium', concept_code='017', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
              value=None
            )
        ),
      intervention_expr=And(
          Observation(
              static=False,
              value_required=False,
              concept=Concept(concept_id=4296791, concept_name='Multidisciplinary care conference', concept_code='384682003', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
              forward_fill=True,
              value=None,
              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None)
            ),
          ProcedureOccurrence(
              static=False,
              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
              concept=Concept(concept_id=44808908, concept_name='Multidisciplinary case management', concept_code='842901000000108', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
              value=None
            )
        ),
      name='RecPlanShareResultsOfRFAssessmentAndPreventiveStrategies',
      url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanShareResultsOfRFAssessmentAndPreventiveStrategies',
      base_criterion=PatientsActiveDuringPeriod()
    )
),
  base_criterion=PatientsActiveDuringPeriod(),
  name='RecCollShareRFOfOlderAdultsPreOPAndRegisterPreventiveStrategies',
  title="Recommendation Collection: Share the results of the screening for POD risk factors among the care team and discuss and register the preventive strategies in the medical records in 'Older Adult Surgical Patients After Preoperative Screening of Risk Factors for POD'",
  url='https://fhir.charite.de/digipod/PlanDefinition/RecCollShareRFOfOlderAdultsPreOPAndRegisterPreventiveStrategies',
  version='0.2.0',
  description='Recommendation collection for older adult patients that were screened for risk factors for postoperative delirium before undergoing a surgical intervention of any type independently of the type of anesthesia: Share the results of the screening for POD risk factors among the care team and discuss and register the preventive strategies in the medical records.',
  package_version='latest',
)
