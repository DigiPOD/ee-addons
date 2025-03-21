from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.criterion.device_exposure import DeviceExposure
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.enum import TimeUnit
from execution_engine.util.logic import *
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept, ValueScalar

from digipod.criterion import (
    BeforeDailyFacesAnxietyScaleAssessment,
    OnFacesAnxietyScaleAssessmentDay,
    PostOperativePatients,
)
from digipod.criterion.patients import AgeLimitPatient
from digipod.criterion.preop_patients import (
    PreOperativePatientsBeforeDayOfSurgery,
    PreOperativePatientsBeforeSurgery,
)

recommendation = Recommendation(
  expr=And(
  And(
      PopulationInterventionPairExpr(
          population_expr=And(
              Not(
                  Or(
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=4182210, concept_name='Dementia', concept_code='52448006', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Disorder', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=1568087, concept_name='Vascular dementia', concept_code='F01', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=1568088, concept_name='Dementia in other diseases classified elsewhere', concept_code='F02', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=1568089, concept_name='Dementia in other diseases classified elsewhere, unspecified severity', concept_code='F02.8', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='4-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=35207114, concept_name='Unspecified dementia', concept_code='F03', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        )
                    )
                ),
              Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                )
            ),
          intervention_expr=TemporalMinCount(
              Measurement(
                  concept=Concept(concept_id=2000000035, concept_name='Faces Anxiety Scale score', concept_code='035', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                  value_required=False,
                  static=False,
                  value=None,
                  timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                  forward_fill=True
                ),
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=And(
                  PostOperativePatients(),
                  PatientsActiveDuringPeriod()
                ),
              threshold=1
            ),
          name='RecPlanAssessFASPostoperatively',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanAssessFASPostoperatively',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      PopulationInterventionPairExpr(
          population_expr=And(
              Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                ),
              Or(
                  Or(
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=4182210, concept_name='Dementia', concept_code='52448006', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Disorder', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=1568087, concept_name='Vascular dementia', concept_code='F01', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=1568088, concept_name='Dementia in other diseases classified elsewhere', concept_code='F02', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=1568089, concept_name='Dementia in other diseases classified elsewhere, unspecified severity', concept_code='F02.8', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='4-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=35207114, concept_name='Unspecified dementia', concept_code='F03', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeSurgery(),
                          threshold=1
                        )
                    ),
                  Or(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000056, concept_name='Confusion Assessment Method score', concept_code='056', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=12.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=3.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000021, concept_name='3-minute Diagnostic Interview for CAM-defined Delirium score', concept_code='021', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000022, concept_name='Confusion Assessment Method for the Intensive Care Unit score', concept_code='022', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=7.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PostOperativePatients(),
                          threshold=1
                        )
                    )
                )
            ),
          intervention_expr=And(
              TemporalMinCount(
                  ProcedureOccurrence(
                      value=None,
                      concept=Concept(concept_id=2000000010, concept_name='Non-pharmacological intervention for anxiety management', concept_code='010', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      static=False,
                      timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=And(
                      PostOperativePatients(),
                      PatientsActiveDuringPeriod()
                    ),
                  threshold=1
                ),
              Or(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=2000000011, concept_name='Verbal management of anxiety', concept_code='011', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=2000000018, concept_name='Avoidance of trigger factors for anxiety', concept_code='018', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4131661, concept_name='Social service interview of patient', concept_code='2658000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=37018932, concept_name='Consultation for palliative care', concept_code='713281006', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4021023, concept_name='Involving family and friends in care', concept_code='225329001', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=4187602, concept_name='Patient education based on identified need', concept_code='372919008', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=None,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4158828, concept_name='Identification of individual values and wishes concerning care', concept_code='370819000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    )
                )
            ),
          name='RecPlanNonPharmaAnxietyMeasuresInPatWithDementiaOrDeliriumPostOP',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaAnxietyMeasuresInPatWithDementiaOrDeliriumPostOP',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      PopulationInterventionPairExpr(
          population_expr=And(
              And(
                  Not(
                      Or(
                          TemporalMinCount(
                              ConditionOccurrence(
                                  concept=Concept(concept_id=4182210, concept_name='Dementia', concept_code='52448006', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Disorder', standard_concept='S', invalid_reason=None),
                                  value_required=False,
                                  static=False,
                                  value=None,
                                  timing=None
                                ),
                              start_time=None,
                              end_time=None,
                              interval_type=None,
                              interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                              threshold=1
                            ),
                          TemporalMinCount(
                              ConditionOccurrence(
                                  concept=Concept(concept_id=1568087, concept_name='Vascular dementia', concept_code='F01', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                                  value_required=False,
                                  static=False,
                                  value=None,
                                  timing=None
                                ),
                              start_time=None,
                              end_time=None,
                              interval_type=None,
                              interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                              threshold=1
                            ),
                          TemporalMinCount(
                              ConditionOccurrence(
                                  concept=Concept(concept_id=1568088, concept_name='Dementia in other diseases classified elsewhere', concept_code='F02', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                                  value_required=False,
                                  static=False,
                                  value=None,
                                  timing=None
                                ),
                              start_time=None,
                              end_time=None,
                              interval_type=None,
                              interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                              threshold=1
                            ),
                          TemporalMinCount(
                              ConditionOccurrence(
                                  concept=Concept(concept_id=1568089, concept_name='Dementia in other diseases classified elsewhere, unspecified severity', concept_code='F02.8', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='4-char nonbill code', standard_concept=None, invalid_reason=None),
                                  value_required=False,
                                  static=False,
                                  value=None,
                                  timing=None
                                ),
                              start_time=None,
                              end_time=None,
                              interval_type=None,
                              interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                              threshold=1
                            ),
                          TemporalMinCount(
                              ConditionOccurrence(
                                  concept=Concept(concept_id=35207114, concept_name='Unspecified dementia', concept_code='F03', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                                  value_required=False,
                                  static=False,
                                  value=None,
                                  timing=None
                                ),
                              start_time=None,
                              end_time=None,
                              interval_type=None,
                              interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                              threshold=1
                            )
                        )
                    ),
                  Or(
                      TemporalMinCount(
                          AgeLimitPatient(
                              min_age_years=70
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        )
                    )
                ),
              Or(
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=1.99998),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=3.99996),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000056, concept_name='Confusion Assessment Method score', concept_code='056', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=11.99988),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000021, concept_name='3-minute Diagnostic Interview for CAM-defined Delirium score', concept_code='021', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000022, concept_name='Confusion Assessment Method for the Intensive Care Unit score', concept_code='022', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=7.99992),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=3.99996),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          BeforeDailyFacesAnxietyScaleAssessment()
                        ),
                      threshold=1
                    )
                ),
              Or(
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000056, concept_name='Confusion Assessment Method score', concept_code='056', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=12.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=3.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000021, concept_name='3-minute Diagnostic Interview for CAM-defined Delirium score', concept_code='021', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000022, concept_name='Confusion Assessment Method for the Intensive Care Unit score', concept_code='022', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=7.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    ),
                  Not(
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              OnFacesAnxietyScaleAssessmentDay(),
                              BeforeDailyFacesAnxietyScaleAssessment()
                            ),
                          threshold=1
                        )
                    )
                ),
              Measurement(
                  concept=Concept(concept_id=2000000035, concept_name='Faces Anxiety Scale score', concept_code='035', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                  value_required=True,
                  static=False,
                  value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                  timing=None,
                  forward_fill=True
                )
            ),
          intervention_expr=And(
              TemporalMinCount(
                  ProcedureOccurrence(
                      value=None,
                      concept=Concept(concept_id=2000000010, concept_name='Non-pharmacological intervention for anxiety management', concept_code='010', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      static=False,
                      timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=And(
                      PostOperativePatients(),
                      PatientsActiveDuringPeriod(),
                      OnFacesAnxietyScaleAssessmentDay()
                    ),
                  threshold=1
                ),
              Or(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=2000000011, concept_name='Verbal management of anxiety', concept_code='011', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=2000000018, concept_name='Avoidance of trigger factors for anxiety', concept_code='018', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4131661, concept_name='Social service interview of patient', concept_code='2658000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=37018932, concept_name='Consultation for palliative care', concept_code='713281006', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4021023, concept_name='Involving family and friends in care', concept_code='225329001', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=4187602, concept_name='Patient education based on identified need', concept_code='372919008', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=None,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    ),
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4158828, concept_name='Identification of individual values and wishes concerning care', concept_code='370819000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod(),
                          OnFacesAnxietyScaleAssessmentDay()
                        ),
                      threshold=1
                    )
                )
            ),
          name='RecPlanNonPharmaMeasuresForAnxietyInPatWithPositiveFASPostOP',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaMeasuresForAnxietyInPatWithPositiveFASPostOP',
          base_criterion=PatientsActiveDuringPeriod()
        )
    ),
  And(
      MinCount(
          PopulationInterventionPairExpr(
              population_expr=Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                ),
              intervention_expr=MinCount(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4301075, concept_name='Cognitive stimulation', concept_code='386241007', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  Or(
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000036, concept_name='Reading or reading to somebody', concept_code='036', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000037, concept_name='Conversation to stimulate cognition', concept_code='037', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000038, concept_name='Playing board games or puzzles', concept_code='038', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000039, concept_name='Singing', concept_code='039', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=4012466, concept_name='Assessment and interpretation of higher cerebral function, cognitive testing', concept_code='113024001', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        )
                    ),
                  threshold=1
                ),
              name='RecPlanCognitiveStimulationPostOP',
              url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanCognitiveStimulationPostOP',
              base_criterion=PatientsActiveDuringPeriod()
            ),
          threshold=1
        ),
      MinCount(
          PopulationInterventionPairExpr(
              population_expr=Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                ),
              intervention_expr=MinCount(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4043216, concept_name='Provision of communication aid', concept_code='228620008', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  Or(
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=4322820, concept_name='Supply of spectacles', concept_code='7128000', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=4085698, concept_name='Hearing aid provision', concept_code='281656009', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=45763977, concept_name='Assistive writing/drafting/drawing board', concept_code='700540009', domain_id='Device', vocabulary_id='SNOMED', concept_class_id='Physical Object', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=4082890, concept_name='Provision of removable denture', concept_code='183117009', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=40482038, concept_name='Request for language interpreter service', concept_code='445075008', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=45771498, concept_name='Communication and information assistive device', concept_code='705371001', domain_id='Device', vocabulary_id='SNOMED', concept_class_id='Physical Object', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        )
                    ),
                  threshold=1
                ),
              name='RecPlanProvisionOfCommunicationAidsPostOP',
              url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanProvisionOfCommunicationAidsPostOP',
              base_criterion=PatientsActiveDuringPeriod()
            ),
          threshold=1
        ),
      MinCount(
          PopulationInterventionPairExpr(
              population_expr=Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                ),
              intervention_expr=MinCount(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=2000000012, concept_name='Non-pharmacological intervention to support the circadian rhythm', concept_code='012', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  Or(
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000040, concept_name='Provision of sleeping mask', concept_code='040', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000041, concept_name='Provision of earplugs at night', concept_code='041', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000042, concept_name='Reduction of noise', concept_code='042', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000043, concept_name='Light exposure during daytime', concept_code='043', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000044, concept_name='Reduction of light exposure at nighttime', concept_code='044', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000045, concept_name='Closing the door of the patient room', concept_code='045', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=37156352, concept_name='Promotion of sleep hygiene', concept_code='1172583004', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000046, concept_name='Performs only emergency procedures at nighttime', concept_code='046', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=2000000047, concept_name='Other non-pharmacological interventions to promote sleep hygiene', concept_code='047', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        )
                    ),
                  threshold=1
                ),
              name='RecPlanNonPharmaInterventionsSupportingCircardianRhythmPostOP',
              url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaInterventionsSupportingCircardianRhythmPostOP',
              base_criterion=PatientsActiveDuringPeriod()
            ),
          threshold=1
        ),
      MinCount(
          PopulationInterventionPairExpr(
              population_expr=Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                ),
              intervention_expr=MinCount(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4038867, concept_name='Reality orientation', concept_code='228547007', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  Or(
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=2000000048, concept_name='Watch', concept_code='048', domain_id='Device', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=2000000049, concept_name='Calendar', concept_code='049', domain_id='Device', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4081701, concept_name='Printed material', concept_code='278211009', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Physical Object', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=4114817, concept_name='Television', concept_code='255712000', domain_id='Device', vocabulary_id='SNOMED', concept_class_id='Physical Object', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=4234434, concept_name='Radio', concept_code='360004001', domain_id='Device', vocabulary_id='SNOMED', concept_class_id='Physical Object', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          DeviceExposure(
                              concept=Concept(concept_id=2000000050, concept_name='Other media', concept_code='050', domain_id='Device', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        )
                    ),
                  threshold=1
                ),
              name='RecPlanDocumentProvisionOrientationAidPostOP',
              url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentProvisionOrientationAidPostOP',
              base_criterion=PatientsActiveDuringPeriod()
            ),
          threshold=1
        )
    ),
  And(
      PopulationInterventionPairExpr(
          population_expr=Or(
              TemporalMinCount(
                  AgeLimitPatient(
                      min_age_years=70
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Observation(
                      concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                      value_required=False,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                )
            ),
          intervention_expr=TemporalMinCount(
              Observation(
                  concept=Concept(concept_id=4103497, concept_name='Ability to mobilize', concept_code='301438001', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                  value_required=False,
                  static=False,
                  value=None,
                  timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                  forward_fill=True
                ),
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=And(
                  PostOperativePatients(),
                  PatientsActiveDuringPeriod()
                ),
              threshold=1
            ),
          name='RecPlanDocumentMobilizationAbilitiesPostoperatively',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentMobilizationAbilitiesPostoperatively',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      ExactCount(
          PopulationInterventionPairExpr(
              population_expr=And(
                  Or(
                      TemporalMinCount(
                          AgeLimitPatient(
                              min_age_years=70
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        )
                    ),
                  Measurement(
                      concept=Concept(concept_id=4103497, concept_name='Ability to mobilize', concept_code='301438001', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                      value_required=False,
                      static=False,
                      value=ValueConcept(value={'concept_id': 4200193, 'concept_name': 'Does not mobilize', 'concept_code': '302045007', 'domain_id': 'Observation', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Clinical Finding', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None,
                      forward_fill=True
                    )
                ),
              intervention_expr=ExactCount(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4251052, concept_name='Physiatric mobilization of joint', concept_code='74251004', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  Or(
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4141768, concept_name='Medical contraindication to procedure', concept_code='266757004', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Context-dependent', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4136190, concept_name='Patient non-compliant - declined intervention / support', concept_code='413311005', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Context-dependent', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=4087481, concept_name='Lack of energy', concept_code='248274002', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=441542, concept_name='Anxiety', concept_code='48694002', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=4329041, concept_name='Pain', concept_code='22253000', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4246495, concept_name='Exhaustion', concept_code='60119000', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=4223938, concept_name='Dizziness', concept_code='404640003', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4128496, concept_name='Reason and justification', concept_code='288830005', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Attribute', standard_concept=None, invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        )
                    ),
                  threshold=1
                ),
              name='RecPlanDocumentMobilizePatientOrDocumentWhyNoMobilizationPostOP',
              url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentMobilizePatientOrDocumentWhyNoMobilizationPostOP',
              base_criterion=PatientsActiveDuringPeriod()
            ),
          threshold=1
        )
    ),
  And(
      PopulationInterventionPairExpr(
          population_expr=Or(
              TemporalMinCount(
                  AgeLimitPatient(
                      min_age_years=70
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Observation(
                      concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                      value_required=False,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                )
            ),
          intervention_expr=TemporalMinCount(
              Observation(
                  concept=Concept(concept_id=4128668, concept_name='Ability to feed self', concept_code='288999009', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                  value_required=False,
                  static=False,
                  value=None,
                  timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                  forward_fill=True
                ),
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=And(
                  PostOperativePatients(),
                  PatientsActiveDuringPeriod()
                ),
              threshold=1
            ),
          name='RecPlanDocumentFeedingAbilitiesPostoperatively',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentFeedingAbilitiesPostoperatively',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      ExactCount(
          PopulationInterventionPairExpr(
              population_expr=And(
                  Or(
                      TemporalMinCount(
                          AgeLimitPatient(
                              min_age_years=70
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Measurement(
                              concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                              value_required=True,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                              timing=None,
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                          threshold=1
                        )
                    ),
                  Measurement(
                      concept=Concept(concept_id=4128668, concept_name='Ability to feed self', concept_code='288999009', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                      value_required=False,
                      static=False,
                      value=ValueConcept(value={'concept_id': 4122440, 'concept_name': 'Does not feed self', 'concept_code': '289003008', 'domain_id': 'Observation', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Clinical Finding', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None,
                      forward_fill=True
                    )
                ),
              intervention_expr=ExactCount(
                  TemporalMinCount(
                      ProcedureOccurrence(
                          value=None,
                          concept=Concept(concept_id=4042005, concept_name='Enteral feeding', concept_code='229912004', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                          static=False,
                          timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=And(
                          PostOperativePatients(),
                          PatientsActiveDuringPeriod()
                        ),
                      threshold=1
                    ),
                  Or(
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4141768, concept_name='Medical contraindication to procedure', concept_code='266757004', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Context-dependent', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ProcedureOccurrence(
                              value=None,
                              concept=Concept(concept_id=4096831, concept_name='Intravenous feeding of patient', concept_code='25156005', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                              static=False,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4160501, concept_name='At increased risk for aspiration', concept_code='371736008', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=4166234, concept_name='Abnormal deglutition', concept_code='47717004', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=4329041, concept_name='Pain', concept_code='22253000', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          Observation(
                              concept=Concept(concept_id=442165, concept_name='Loss of appetite', concept_code='79890006', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                              forward_fill=True
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=46271381, concept_name='Digestive system reflux', concept_code='709493000', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Clinical Finding', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        ),
                      TemporalMinCount(
                          ConditionOccurrence(
                              concept=Concept(concept_id=27674, concept_name='Nausea and vomiting', concept_code='16932000', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Disorder', standard_concept='S', invalid_reason=None),
                              value_required=False,
                              static=False,
                              value=None,
                              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=And(
                              PostOperativePatients(),
                              PatientsActiveDuringPeriod()
                            ),
                          threshold=1
                        )
                    ),
                  threshold=1
                ),
              name='RecPlanDocumentFeedEnterallyPatientOrDocumentWhyNoFeedingPostOP',
              url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentFeedEnterallyPatientOrDocumentWhyNoFeedingPostOP',
              base_criterion=PatientsActiveDuringPeriod()
            ),
          threshold=1
        ),
      PopulationInterventionPairExpr(
          population_expr=Or(
              TemporalMinCount(
                  AgeLimitPatient(
                      min_age_years=70
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Observation(
                      concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                      value_required=False,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                )
            ),
          intervention_expr=TemporalMinCount(
              Observation(
                  concept=Concept(concept_id=4185237, concept_name='Deglutition', concept_code='54731003', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                  value_required=False,
                  static=False,
                  value=None,
                  timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                  forward_fill=True
                ),
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=And(
                  PostOperativePatients(),
                  PatientsActiveDuringPeriod()
                ),
              threshold=1
            ),
          name='RecPlanDocumentDeglutitionAbilitiesPostoperatively',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentDeglutitionAbilitiesPostoperatively',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      PopulationInterventionPairExpr(
          population_expr=And(
              Or(
                  TemporalMinCount(
                      AgeLimitPatient(
                          min_age_years=70
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Measurement(
                          concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          value_required=True,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    ),
                  TemporalMinCount(
                      Observation(
                          concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                          value_required=False,
                          static=False,
                          value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                          timing=None,
                          forward_fill=True
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                      threshold=1
                    )
                ),
              Measurement(
                  concept=Concept(concept_id=4185237, concept_name='Deglutition', concept_code='54731003', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                  value_required=False,
                  static=False,
                  value=ValueConcept(value={'concept_id': 4166234, 'concept_name': 'Abnormal deglutition', 'concept_code': '47717004', 'domain_id': 'Observation', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Clinical Finding', 'standard_concept': 'S', 'invalid_reason': None}),
                  timing=None,
                  forward_fill=True
                )
            ),
          intervention_expr=And(
              TemporalMinCount(
                  ProcedureOccurrence(
                      value=None,
                      concept=Concept(concept_id=4210275, concept_name='Dysphagia therapy regime', concept_code='311569007', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                      static=False,
                      timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=And(
                      PostOperativePatients(),
                      PatientsActiveDuringPeriod(),
                      OnFacesAnxietyScaleAssessmentDay()
                    ),
                  threshold=1
                ),
              TemporalMinCount(
                  ProcedureOccurrence(
                      value=None,
                      concept=Concept(concept_id=763733, concept_name='Modification of nutritional regime', concept_code='445341000124100', domain_id='Procedure', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                      static=False,
                      timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None})
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=And(
                      PostOperativePatients(),
                      PatientsActiveDuringPeriod(),
                      OnFacesAnxietyScaleAssessmentDay()
                    ),
                  threshold=1
                )
            ),
          name='RecPlanDeglutitionRelatedInterventionsPostoperatively',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanDeglutitionRelatedInterventionsPostoperatively',
          base_criterion=PatientsActiveDuringPeriod()
        ),
      PopulationInterventionPairExpr(
          population_expr=Or(
              TemporalMinCount(
                  AgeLimitPatient(
                      min_age_years=70
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=4199571, concept_name='American Society of Anesthesiologists physical status class', concept_code='302132005', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept='S', invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=2000000009, concept_name='Result of Charlson Comorbidity Index', concept_code='009', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=37017178, concept_name='Mini-Cog test score', concept_code='713408000', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=40491929, concept_name='Mini-mental state examination score', concept_code='447316007', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      concept=Concept(concept_id=44804259, concept_name="Addenbrooke's cognitive examination revised - score", concept_code='711061000000109', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      value_required=True,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                ),
              TemporalMinCount(
                  Observation(
                      concept=Concept(concept_id=43054915, concept_name='Total score [MoCA]', concept_code='72172-0', domain_id='Observation', vocabulary_id='LOINC', concept_class_id='Survey', standard_concept='S', invalid_reason=None),
                      value_required=False,
                      static=False,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
                      timing=None,
                      forward_fill=True
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
                  threshold=1
                )
            ),
          intervention_expr=TemporalMinCount(
              Observation(
                  concept=Concept(concept_id=37397340, concept_name='Mouth care', concept_code='717778001', domain_id='Observation', vocabulary_id='SNOMED', concept_class_id='Procedure', standard_concept='S', invalid_reason=None),
                  value_required=False,
                  static=False,
                  value=None,
                  timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, interval={'unit': TimeUnit.DAY, 'value': 1, 'value_min': None, 'value_max': None}),
                  forward_fill=True
                ),
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=And(
                  PostOperativePatients(),
                  PatientsActiveDuringPeriod()
                ),
              threshold=1
            ),
          name='RecPlanOralCareRelatedInterventionsPostoperatively',
          url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanOralCareRelatedInterventionsPostoperatively',
          base_criterion=PatientsActiveDuringPeriod()
        )
    )
),
  base_criterion=PatientsActiveDuringPeriod(),
  name='RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD',
  title="Recommendation Collection: Perform a bundle of non-pharmacological interventions once a day postoperatively in different populations of 'Adult Surgical Patients At Risk For POD'",
  url='https://fhir.charite.de/digipod/PlanDefinition/RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD',
  version='0.1.0',
  description='Recommendation collection for different populations of adult patients that were at risk for postoperative delirium before undergoing a surgical intervention of any type independently of the type of anesthesia: Perform different non-pharmacological interventions (related to anxiety, nutrition, mobilization, and cognition) as bundle once a day postoperatively until discharge.',
  package_version='latest',
)
