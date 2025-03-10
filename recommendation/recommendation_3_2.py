from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    PersonalWindowTemporalIndicatorCombination,
    TemporalIndicatorCombination,
)
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept
from execution_engine.util.value.time import ValueCount
from execution_engine.util.value.value import ValueScalar

from digipod.criterion import PatientsBeforeFirstDexAdministration
from digipod.criterion.patients import AgeLimitPatient
from digipod.criterion.preop_patients import PreOperativePatientsBeforeSurgery

recommendation = Recommendation(
    pi_pairs=[
        PopulationInterventionPair(
            name="RecPlanSelectProphylacticDexAdministrationInPatsWithoutDementia",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanSelectProphylacticDexAdministrationInPatsWithoutDementia",
            base_criterion=PatientsActiveDuringPeriod(),
            population=LogicalCriterionCombination.And(
                LogicalCriterionCombination.And(
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PreOperativePatientsBeforeSurgery(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=AgeLimitPatient(),
                    ),
                    LogicalCriterionCombination.Not(
                        LogicalCriterionCombination.Or(
                            PersonalWindowTemporalIndicatorCombination(
                                interval_criterion=PreOperativePatientsBeforeSurgery(),
                                operator=TemporalIndicatorCombination.Operator(
                                    operator="AT_LEAST", threshold=1
                                ),
                                criterion=ConditionOccurrence(
                                    concept=Concept(
                                        concept_id=4182210,
                                        concept_name="Dementia",
                                        concept_code="52448006",
                                        domain_id="Condition",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Disorder",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    ),
                                    static=False,
                                ),
                            ),
                            PersonalWindowTemporalIndicatorCombination(
                                interval_criterion=PreOperativePatientsBeforeSurgery(),
                                operator=TemporalIndicatorCombination.Operator(
                                    operator="AT_LEAST", threshold=1
                                ),
                                criterion=ConditionOccurrence(
                                    concept=Concept(
                                        concept_id=1568087,
                                        concept_name="Vascular dementia",
                                        concept_code="F01",
                                        domain_id="Condition",
                                        vocabulary_id="ICD10CM",
                                        concept_class_id="3-char nonbill code",
                                        standard_concept=None,
                                        invalid_reason=None,
                                    ),
                                    static=False,
                                ),
                            ),
                            PersonalWindowTemporalIndicatorCombination(
                                interval_criterion=PreOperativePatientsBeforeSurgery(),
                                operator=TemporalIndicatorCombination.Operator(
                                    operator="AT_LEAST", threshold=1
                                ),
                                criterion=ConditionOccurrence(
                                    concept=Concept(
                                        concept_id=1568088,
                                        concept_name="Dementia in other diseases classified elsewhere",
                                        concept_code="F02",
                                        domain_id="Condition",
                                        vocabulary_id="ICD10CM",
                                        concept_class_id="3-char nonbill code",
                                        standard_concept=None,
                                        invalid_reason=None,
                                    ),
                                    static=False,
                                ),
                            ),
                            PersonalWindowTemporalIndicatorCombination(
                                interval_criterion=PreOperativePatientsBeforeSurgery(),
                                operator=TemporalIndicatorCombination.Operator(
                                    operator="AT_LEAST", threshold=1
                                ),
                                criterion=ConditionOccurrence(
                                    concept=Concept(
                                        concept_id=1568089,
                                        concept_name="Dementia in other diseases classified elsewhere, unspecified severity",
                                        concept_code="F02.8",
                                        domain_id="Condition",
                                        vocabulary_id="ICD10CM",
                                        concept_class_id="4-char nonbill code",
                                        standard_concept=None,
                                        invalid_reason=None,
                                    ),
                                    static=False,
                                ),
                            ),
                            PersonalWindowTemporalIndicatorCombination(
                                interval_criterion=PreOperativePatientsBeforeSurgery(),
                                operator=TemporalIndicatorCombination.Operator(
                                    operator="AT_LEAST", threshold=1
                                ),
                                criterion=ConditionOccurrence(
                                    concept=Concept(
                                        concept_id=35207114,
                                        concept_name="Unspecified dementia",
                                        concept_code="F03",
                                        domain_id="Condition",
                                        vocabulary_id="ICD10CM",
                                        concept_class_id="3-char nonbill code",
                                        standard_concept=None,
                                        invalid_reason=None,
                                    ),
                                    static=False,
                                ),
                            ),
                        ),
                    ),
                ),
                LogicalCriterionCombination.Or(
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000012,
                                concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
                                concept_code="016",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueScalar(
                                unit=None, value=None, value_min=None, value_max=1.99998
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000012,
                                concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
                                concept_code="016",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000012,
                                concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
                                concept_code="016",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=4127785,
                                    concept_name="Weakly positive",
                                    concept_code="260408008",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000018,
                                concept_name="Intensive Care Delirium Screening Checklist score (observable entity)",
                                concept_code="1351995008",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueScalar(
                                unit=None, value=None, value_min=None, value_max=3.99996
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000018,
                                concept_name="Intensive Care Delirium Screening Checklist score (observable entity)",
                                concept_code="1351995008",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000018,
                                concept_name="Intensive Care Delirium Screening Checklist score (observable entity)",
                                concept_code="1351995008",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=4127785,
                                    concept_name="Weakly positive",
                                    concept_code="260408008",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000013,
                                concept_name="Confusion Assessment Method score (observable entity)",
                                concept_code="1351493007",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000015,
                                concept_name="Delirium Rating Scale score",
                                concept_code="019",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueScalar(
                                unit=None,
                                value=None,
                                value_min=None,
                                value_max=11.99988,
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000015,
                                concept_name="Delirium Rating Scale score",
                                concept_code="019",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000015,
                                concept_name="Delirium Rating Scale score",
                                concept_code="019",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=4127785,
                                    concept_name="Weakly positive",
                                    concept_code="260408008",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000016,
                                concept_name="Delirium Observation Scale score",
                                concept_code="020",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueScalar(
                                unit=None, value=None, value_min=None, value_max=2.99997
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000016,
                                concept_name="Delirium Observation Scale score",
                                concept_code="020",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000016,
                                concept_name="Delirium Observation Scale score",
                                concept_code="020",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=4127785,
                                    concept_name="Weakly positive",
                                    concept_code="260408008",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000014,
                                concept_name="3-minute Diagnostic Interview for CAM-defined Delirium score",
                                concept_code="021",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000017,
                                concept_name="Confusion Assessment Method for the Intensive Care Unit score",
                                concept_code="022",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000019,
                                concept_name="Delirium Detection Score score",
                                concept_code="023",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueScalar(
                                unit=None, value=None, value_min=None, value_max=7.99992
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000019,
                                concept_name="Delirium Detection Score score",
                                concept_code="023",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=2000000019,
                                concept_name="Delirium Detection Score score",
                                concept_code="023",
                                domain_id="Measurement",
                                vocabulary_id="DIGIPOD",
                                concept_class_id="Custom",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=4127785,
                                    concept_name="Weakly positive",
                                    concept_code="260408008",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=3662221,
                                concept_name="4AT (4 A's Test) score",
                                concept_code="1239211000000103",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Observable Entity",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueScalar(
                                unit=None, value=None, value_min=None, value_max=3.99996
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=3662221,
                                concept_name="4AT (4 A's Test) score",
                                concept_code="1239211000000103",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Observable Entity",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=9189,
                                    concept_name="Negative",
                                    concept_code="260385009",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PatientsBeforeFirstDexAdministration(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=Measurement(
                            concept=Concept(
                                concept_id=3662221,
                                concept_name="4AT (4 A's Test) score",
                                concept_code="1239211000000103",
                                domain_id="Measurement",
                                vocabulary_id="SNOMED",
                                concept_class_id="Observable Entity",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            value=ValueConcept(
                                value=Concept(
                                    concept_id=4127785,
                                    concept_name="Weakly positive",
                                    concept_code="260408008",
                                    domain_id="Meas Value",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Qualifier Value",
                                    standard_concept="S",
                                    invalid_reason=None,
                                )
                            ),
                        ),
                    ),
                ),
                LogicalCriterionCombination.Or(
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000012,
                                    concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
                                    concept_code="016",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueScalar(
                                    unit=None, value=None, value_min=2.0, value_max=None
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000012,
                                    concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
                                    concept_code="016",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000018,
                                    concept_name="Intensive Care Delirium Screening Checklist score (observable entity)",
                                    concept_code="1351995008",
                                    domain_id="Measurement",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueScalar(
                                    unit=None, value=None, value_min=4.0, value_max=None
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000018,
                                    concept_name="Intensive Care Delirium Screening Checklist score (observable entity)",
                                    concept_code="1351995008",
                                    domain_id="Measurement",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000013,
                                    concept_name="Confusion Assessment Method score (observable entity)",
                                    concept_code="1351493007",
                                    domain_id="Measurement",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000015,
                                    concept_name="Delirium Rating Scale score",
                                    concept_code="019",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueScalar(
                                    unit=None,
                                    value=None,
                                    value_min=12.0,
                                    value_max=None,
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000015,
                                    concept_name="Delirium Rating Scale score",
                                    concept_code="019",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000016,
                                    concept_name="Delirium Observation Scale score",
                                    concept_code="020",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueScalar(
                                    unit=None, value=None, value_min=3.0, value_max=None
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000016,
                                    concept_name="Delirium Observation Scale score",
                                    concept_code="020",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000014,
                                    concept_name="3-minute Diagnostic Interview for CAM-defined Delirium score",
                                    concept_code="021",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000017,
                                    concept_name="Confusion Assessment Method for the Intensive Care Unit score",
                                    concept_code="022",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000019,
                                    concept_name="Delirium Detection Score score",
                                    concept_code="023",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueScalar(
                                    unit=None, value=None, value_min=7.0, value_max=None
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=2000000019,
                                    concept_name="Delirium Detection Score score",
                                    concept_code="023",
                                    domain_id="Measurement",
                                    vocabulary_id="DIGIPOD",
                                    concept_class_id="Custom",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=3662221,
                                    concept_name="4AT (4 A's Test) score",
                                    concept_code="1239211000000103",
                                    domain_id="Measurement",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Observable Entity",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueScalar(
                                    unit=None, value=None, value_min=4.0, value_max=None
                                ),
                            ),
                        ),
                    ),
                    LogicalCriterionCombination.Not(
                        PersonalWindowTemporalIndicatorCombination(
                            interval_criterion=PatientsBeforeFirstDexAdministration(),
                            operator=TemporalIndicatorCombination.Operator(
                                operator="AT_LEAST", threshold=1
                            ),
                            criterion=Measurement(
                                concept=Concept(
                                    concept_id=3662221,
                                    concept_name="4AT (4 A's Test) score",
                                    concept_code="1239211000000103",
                                    domain_id="Measurement",
                                    vocabulary_id="SNOMED",
                                    concept_class_id="Observable Entity",
                                    standard_concept=None,
                                    invalid_reason=None,
                                ),
                                value=ValueConcept(
                                    value=Concept(
                                        concept_id=9191,
                                        concept_name="Positive",
                                        concept_code="10828004",
                                        domain_id="Meas Value",
                                        vocabulary_id="SNOMED",
                                        concept_class_id="Qualifier Value",
                                        standard_concept="S",
                                        invalid_reason=None,
                                    )
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            intervention=LogicalCriterionCombination.And(
                LogicalCriterionCombination.And(
                    Observation(
                        concept=Concept(
                            concept_id=2099999999,
                            concept_name="Administration of prophylactic dexmedetomidine",
                            concept_code="024",
                            domain_id="Observation",
                            vocabulary_id="DIGIPOD",
                            concept_class_id="Custom",
                            standard_concept=None,
                            invalid_reason=None,
                        ),
                        timing=Timing(
                            count=ValueCount(
                                unit=None, value=None, value_min=1, value_max=None
                            ),
                            duration=None,
                            frequency=None,
                            interval=None,
                        ),
                        override_value_required=False,
                    ),
                ),
            ),
        ),
        PopulationInterventionPair(
            name="RecPlanSelectProphylacticDexAdministrationInPatsWithDementia",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanSelectProphylacticDexAdministrationInPatsWithDementia",
            base_criterion=PatientsActiveDuringPeriod(),
            population=LogicalCriterionCombination.And(
                PersonalWindowTemporalIndicatorCombination(
                    interval_criterion=PreOperativePatientsBeforeSurgery(),
                    operator=TemporalIndicatorCombination.Operator(
                        operator="AT_LEAST", threshold=1
                    ),
                    criterion=AgeLimitPatient(),
                ),
                LogicalCriterionCombination.Or(
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PreOperativePatientsBeforeSurgery(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=ConditionOccurrence(
                            concept=Concept(
                                concept_id=4182210,
                                concept_name="Dementia",
                                concept_code="52448006",
                                domain_id="Condition",
                                vocabulary_id="SNOMED",
                                concept_class_id="Disorder",
                                standard_concept="S",
                                invalid_reason=None,
                            ),
                            static=False,
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PreOperativePatientsBeforeSurgery(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=ConditionOccurrence(
                            concept=Concept(
                                concept_id=1568087,
                                concept_name="Vascular dementia",
                                concept_code="F01",
                                domain_id="Condition",
                                vocabulary_id="ICD10CM",
                                concept_class_id="3-char nonbill code",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            static=False,
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PreOperativePatientsBeforeSurgery(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=ConditionOccurrence(
                            concept=Concept(
                                concept_id=1568088,
                                concept_name="Dementia in other diseases classified elsewhere",
                                concept_code="F02",
                                domain_id="Condition",
                                vocabulary_id="ICD10CM",
                                concept_class_id="3-char nonbill code",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            static=False,
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PreOperativePatientsBeforeSurgery(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=ConditionOccurrence(
                            concept=Concept(
                                concept_id=1568089,
                                concept_name="Dementia in other diseases classified elsewhere, unspecified severity",
                                concept_code="F02.8",
                                domain_id="Condition",
                                vocabulary_id="ICD10CM",
                                concept_class_id="4-char nonbill code",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            static=False,
                        ),
                    ),
                    PersonalWindowTemporalIndicatorCombination(
                        interval_criterion=PreOperativePatientsBeforeSurgery(),
                        operator=TemporalIndicatorCombination.Operator(
                            operator="AT_LEAST", threshold=1
                        ),
                        criterion=ConditionOccurrence(
                            concept=Concept(
                                concept_id=35207114,
                                concept_name="Unspecified dementia",
                                concept_code="F03",
                                domain_id="Condition",
                                vocabulary_id="ICD10CM",
                                concept_class_id="3-char nonbill code",
                                standard_concept=None,
                                invalid_reason=None,
                            ),
                            static=False,
                        ),
                    ),
                ),
            ),
            intervention=LogicalCriterionCombination.And(
                LogicalCriterionCombination.And(
                    Observation(
                        concept=Concept(
                            concept_id=2099999999,
                            concept_name="Administration of prophylactic dexmedetomidine",
                            concept_code="024",
                            domain_id="Observation",
                            vocabulary_id="DIGIPOD",
                            concept_class_id="Custom",
                            standard_concept=None,
                            invalid_reason=None,
                        ),
                        timing=Timing(
                            count=ValueCount(
                                unit=None, value=None, value_min=1, value_max=None
                            ),
                            duration=None,
                            frequency=None,
                            interval=None,
                        ),
                        override_value_required=False,
                    ),
                ),
            ),
        ),
    ],
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE",
    title="Recommendation Collection: Select 'prophylactic' if you administer dexmedetomidine intra- or postoperatively with the aim to prevent postoperative delirium after having balanced benefits and side effects in 'General Adult Surgical Patients With Dementia Preoperatively' or 'General Adult Surgical Patients Without Dementia Preoperatively nor Delirium Before Dexmedetomidine Administration'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE",
    version="0.4.0",
    description="Recommendation collection for adult patients getting dexmedetomidine during or after a surgical intervention of any type and independently of the type of anesthesia with the aim to prevent postoperative delirium (POD): Select 'prophylactic' if you administer dexmedetomidine with the aim to prevent postoperative delirium after having balanced benefits and side effects.",
    package_version="latest",
)
