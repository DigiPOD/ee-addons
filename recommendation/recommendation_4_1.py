from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.logic import *
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept

from digipod.criterion.patients import AgeLimitPatient
from digipod.criterion.preop_patients import PreOperativePatientsBeforeDayOfSurgery

recommendation = Recommendation(
  expr=And(
  MinCount(
      PopulationInterventionPairExpr(
          population_expr=TemporalMinCount(
              AgeLimitPatient(
                  min_age_years=70
                ),
              threshold=1,
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=PreOperativePatientsBeforeDayOfSurgery()
            ),
          intervention_expr=MinCount(
              ProcedureOccurrence(
                  timing=None,
                  value=None,
                  concept=Concept(concept_id=2000000017, concept_name='Assessment for risk of post-operative delirium', concept_code='017', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                  static=False
                ),
              And(
                  And(
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4314723, concept_name='Cardiac assessment', concept_code='425315000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4021179, concept_name='Neurological assessment', concept_code='225398001', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4181638, concept_name='Cardiovascular examination and evaluation', concept_code='43038000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      Measurement(
                          value=None,
                          concept=Concept(concept_id=4064918, concept_name='Diabetes mellitus screening', concept_code='171183004', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          forward_fill=True,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value_required=False
                        ),
                      Measurement(
                          value=None,
                          concept=Concept(concept_id=4062491, concept_name='Anemia screening', concept_code='171201007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          forward_fill=True,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value_required=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=46273905, concept_name='Assessment of depressed mood', concept_code='710846002', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4021323, concept_name='Pain assessment', concept_code='225399009', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=46272472, concept_name='Assessment of anxiety', concept_code='710841007', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=762506, concept_name='Assessment of substance use', concept_code='428211000124100', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4012466, concept_name='Assessment and interpretation of higher cerebral function, cognitive testing', concept_code='113024001', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=43021483, concept_name='Assessment of dementia', concept_code='473203000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4046889, concept_name='Frail elderly assessment', concept_code='134427001', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4158084, concept_name='Determination of existing sensory impairments', concept_code='370837004', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4149297, concept_name='Nutritional assessment', concept_code='310243009', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4244831, concept_name='Medication administration assessment', concept_code='396073008', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      Measurement(
                          value=None,
                          concept=Concept(concept_id=4193783, concept_name='Electrolytes measurement', concept_code='79301008', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          forward_fill=True,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value_required=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4258123, concept_name='Evaluation of oral and pharyngeal swallowing function', concept_code='440363007', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      Measurement(
                          value=None,
                          concept=Concept(concept_id=35621948, concept_name='Anticholinergic Cognitive Burden Scale', concept_code='763240001', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Staging / Scales', standard_concept='S', invalid_reason=None),
                          static=False,
                          forward_fill=True,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value_required=False
                        )
                    ),
                  Or(
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4057399, concept_name='Pre-anesthetic assessment', concept_code='182770003', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=46272237, concept_name='Assessment of risk for dehydration', concept_code='710567009', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=46272234, concept_name='Assessment of risk for impaired nutritional status', concept_code='710563008', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        ),
                      ProcedureOccurrence(
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
                          value=None,
                          concept=Concept(concept_id=4155294, concept_name='Assessment of hypovolemia risk factors', concept_code='372114004', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False
                        )
                    )
                ),
              threshold=1
            ),
          name='RecPlanScreeningOfRFInOlderPatientsPreOP',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanScreeningOfRFInOlderPatientsPreOP',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      threshold=1
    ),
  PopulationInterventionPairExpr(
      population_expr=And(
          TemporalMinCount(
              AgeLimitPatient(
                  min_age_years=70
                ),
              threshold=1,
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=PreOperativePatientsBeforeDayOfSurgery()
            ),
          TemporalMinCount(
              ProcedureOccurrence(
                  timing=None,
                  value=None,
                  concept=Concept(concept_id=2000000017, concept_name='Assessment for risk of post-operative delirium', concept_code='017', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                  static=False
                ),
              threshold=1,
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=PreOperativePatientsBeforeDayOfSurgery()
            ),
          TemporalMinCount(
              Observation(
                  value=ValueConcept(value={'concept_id': 4181412, 'concept_name': 'Present', 'concept_code': '52101004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                  concept=Concept(concept_id=2000000007, concept_name='Optimizable preoperative risk factor', concept_code='007', domain_id='Observation', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                  static=False,
                  forward_fill=True,
                  timing=None,
                  value_required=False
                ),
              threshold=1,
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=PreOperativePatientsBeforeDayOfSurgery()
            )
        ),
      intervention_expr=Observation(
          value=None,
          concept=Concept(concept_id=2000000008, concept_name='Preoperative risk factor optimization', concept_code='008', domain_id='Observation', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
          static=False,
          forward_fill=True,
          timing=None,
          value_required=False
        ),
      name='RecPlanOptimizationOfPreOPStatusInOlderPatPreoperatively',
      url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanOptimizationOfPreOPStatusInOlderPatPreoperatively',
      base_criterion=PatientsActiveDuringPeriod()
    )
),
  base_criterion=PatientsActiveDuringPeriod(),
  name='RecCollPreoperativeRFAssessmentAndOptimization',
  title="Recommendation Collection: Assess risk factors for postoperative delirium and address patient's needs to optimize the preoperative status in 'Older Adult Surgical Patients Preoperatively' & 'Older Adult Surgical Patients With Optimizable Risk Factors Identified Preoperatively'",
  url='https://fhir.charite.de/digipod/PlanDefinition/RecCollPreoperativeRFAssessmentAndOptimization',
  version='0.3.0',
  description="Recommendation collection for older adult patients before undergoing a surgical intervention of any type independently of the type of anesthesia: Assess risk factors for postoperative delirium (POD) and address patient's needs to optimize the preoperative status",
  package_version='latest',
)
