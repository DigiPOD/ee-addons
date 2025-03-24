from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.logic import *
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept, ValueScalar

from digipod.criterion import (
    IntraOrPostOperativePatients,
    PatientsBeforeFirstDexAdministration,
)
from digipod.criterion.patients import AgeLimitPatient
from digipod.criterion.preop_patients import PreOperativePatientsBeforeSurgery

recommendation = Recommendation(
  expr=And(
  PopulationInterventionPairExpr(
      population_expr=And(
          And(
              TemporalMinCount(
                  AgeLimitPatient(
                      min_age_years=18
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeSurgery(),
                  threshold=1
                ),
              Not(
                  Or(
                      TemporalMinCount(
                          ConditionOccurrence(
                              static=False,
                              value_required=False,
                              concept=Concept(concept_id=4182210, concept_name='Dementia', concept_code='52448006', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Disorder', standard_concept='S', invalid_reason=None),
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
                              static=False,
                              value_required=False,
                              concept=Concept(concept_id=1568087, concept_name='Vascular dementia', concept_code='F01', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
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
                              static=False,
                              value_required=False,
                              concept=Concept(concept_id=1568088, concept_name='Dementia in other diseases classified elsewhere', concept_code='F02', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
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
                              static=False,
                              value_required=False,
                              concept=Concept(concept_id=1568089, concept_name='Dementia in other diseases classified elsewhere, unspecified severity', concept_code='F02.8', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='4-char nonbill code', standard_concept=None, invalid_reason=None),
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
                              static=False,
                              value_required=False,
                              concept=Concept(concept_id=35207114, concept_name='Unspecified dementia', concept_code='F03', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                              value=None,
                              timing=None
                            ),
                          start_time=None,
                          end_time=None,
                          interval_type=None,
                          interval_criterion=PreOperativePatientsBeforeSurgery(),
                          threshold=1
                        )
                    )
                )
            ),
          Or(
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=1.99998),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=3.99996),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000056, concept_name='Confusion Assessment Method score', concept_code='056', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=11.99988),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000021, concept_name='3-minute Diagnostic Interview for CAM-defined Delirium score', concept_code='021', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000022, concept_name='Confusion Assessment Method for the Intensive Care Unit score', concept_code='022', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=7.99992),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueScalar(unit=None, value=None, value_min=None, value_max=3.99996),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 9189, 'concept_name': 'Negative', 'concept_code': '260385009', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                ),
              TemporalMinCount(
                  Measurement(
                      static=False,
                      value_required=True,
                      concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                      forward_fill=True,
                      value=ValueConcept(value={'concept_id': 4127785, 'concept_name': 'Weakly positive', 'concept_code': '260408008', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PatientsBeforeFirstDexAdministration(),
                  threshold=1
                )
            ),
          Or(
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000016, concept_name='Nursing Delirium Screening Scale (NU-DESC) score', concept_code='016', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000055, concept_name='Intensive Care Delirium Screening Checklist score', concept_code='055', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000056, concept_name='Confusion Assessment Method score', concept_code='056', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueScalar(unit=None, value=None, value_min=12.0, value_max=None),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000019, concept_name='Delirium Rating Scale score', concept_code='019', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueScalar(unit=None, value=None, value_min=3.0, value_max=None),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000020, concept_name='Delirium Observation Scale score', concept_code='020', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000021, concept_name='3-minute Diagnostic Interview for CAM-defined Delirium score', concept_code='021', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000022, concept_name='Confusion Assessment Method for the Intensive Care Unit score', concept_code='022', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueScalar(unit=None, value=None, value_min=7.0, value_max=None),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=2000000023, concept_name='Delirium Detection Score score', concept_code='023', domain_id='Measurement', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                ),
              Not(
                  TemporalMinCount(
                      Measurement(
                          static=False,
                          value_required=True,
                          concept=Concept(concept_id=3662221, concept_name="4AT (4 A's Test) score", concept_code='1239211000000103', domain_id='Measurement', vocabulary_id='SNOMED', concept_class_id='Observable Entity', standard_concept=None, invalid_reason=None),
                          forward_fill=True,
                          value=ValueConcept(value={'concept_id': 9191, 'concept_name': 'Positive', 'concept_code': '10828004', 'domain_id': 'Meas Value', 'vocabulary_id': 'SNOMED', 'concept_class_id': 'Qualifier Value', 'standard_concept': 'S', 'invalid_reason': None}),
                          timing=None
                        ),
                      start_time=None,
                      end_time=None,
                      interval_type=None,
                      interval_criterion=PatientsBeforeFirstDexAdministration(),
                      threshold=1
                    )
                )
            )
        ),
      intervention_expr=TemporalMinCount(
          ProcedureOccurrence(
              static=False,
              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
              concept=Concept(concept_id=2000000024, concept_name='Administration of prophylactic dexmedetomidine', concept_code='024', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
              value=None
            ),
          start_time=None,
          end_time=None,
          interval_type=None,
          interval_criterion=IntraOrPostOperativePatients(),
          threshold=1
        ),
      name='RecPlanSelectProphylacticDexAdministrationInPatsWithoutDementia',
      url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanSelectProphylacticDexAdministrationInPatsWithoutDementia',
      base_criterion=PatientsActiveDuringPeriod()
    ),
  PopulationInterventionPairExpr(
      population_expr=And(
          TemporalMinCount(
              AgeLimitPatient(
                  min_age_years=18
                ),
              start_time=None,
              end_time=None,
              interval_type=None,
              interval_criterion=PreOperativePatientsBeforeSurgery(),
              threshold=1
            ),
          Or(
              TemporalMinCount(
                  ConditionOccurrence(
                      static=False,
                      value_required=False,
                      concept=Concept(concept_id=4182210, concept_name='Dementia', concept_code='52448006', domain_id='Condition', vocabulary_id='SNOMED', concept_class_id='Disorder', standard_concept='S', invalid_reason=None),
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
                      static=False,
                      value_required=False,
                      concept=Concept(concept_id=1568087, concept_name='Vascular dementia', concept_code='F01', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
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
                      static=False,
                      value_required=False,
                      concept=Concept(concept_id=1568088, concept_name='Dementia in other diseases classified elsewhere', concept_code='F02', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
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
                      static=False,
                      value_required=False,
                      concept=Concept(concept_id=1568089, concept_name='Dementia in other diseases classified elsewhere, unspecified severity', concept_code='F02.8', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='4-char nonbill code', standard_concept=None, invalid_reason=None),
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
                      static=False,
                      value_required=False,
                      concept=Concept(concept_id=35207114, concept_name='Unspecified dementia', concept_code='F03', domain_id='Condition', vocabulary_id='ICD10CM', concept_class_id='3-char nonbill code', standard_concept=None, invalid_reason=None),
                      value=None,
                      timing=None
                    ),
                  start_time=None,
                  end_time=None,
                  interval_type=None,
                  interval_criterion=PreOperativePatientsBeforeSurgery(),
                  threshold=1
                )
            )
        ),
      intervention_expr=TemporalMinCount(
          ProcedureOccurrence(
              static=False,
              timing=Timing(count={'unit': None, 'value': None, 'value_min': 1, 'value_max': None}, duration=None, frequency=None, interval=None),
              concept=Concept(concept_id=2000000024, concept_name='Administration of prophylactic dexmedetomidine', concept_code='024', domain_id='Procedure', vocabulary_id='DIGIPOD', concept_class_id='Custom', standard_concept=None, invalid_reason=None),
              value=None
            ),
          start_time=None,
          end_time=None,
          interval_type=None,
          interval_criterion=IntraOrPostOperativePatients(),
          threshold=1
        ),
      name='RecPlanSelectProphylacticDexAdministrationInPatsWithDementia',
      url='https://fhir.charite.de/digipod/PlanDefinition/RecPlanSelectProphylacticDexAdministrationInPatsWithDementia',
      base_criterion=PatientsActiveDuringPeriod()
    )
),
  base_criterion=PatientsActiveDuringPeriod(),
  name='RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE',
  title="Recommendation Collection: Select 'prophylactic' if you administer dexmedetomidine intra- or postoperatively with the aim to prevent postoperative delirium after having balanced benefits and side effects in 'General Adult Surgical Patients With Dementia Preoperatively' or 'General Adult Surgical Patients Without Dementia Preoperatively nor Delirium Before Dexmedetomidine Administration'",
  url='https://fhir.charite.de/digipod/PlanDefinition/RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE',
  version='0.4.0',
  description="Recommendation collection for adult patients getting dexmedetomidine during or after a surgical intervention of any type and independently of the type of anesthesia with the aim to prevent postoperative delirium (POD): Select 'prophylactic' if you administer dexmedetomidine with the aim to prevent postoperative delirium after having balanced benefits and side effects.",
  package_version='latest',
)
