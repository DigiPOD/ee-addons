from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.criterion.device_exposure import DeviceExposure
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.util import logic
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
from digipod.terminology import custom_concepts


def PostOperative(arg: logic.BaseExpr) -> logic.TemporalMinCount:
    """
    Applies a post-operative temporal constraint ensuring that the given argument
    occurred at least once during the post-operative period.
    """
    return logic.TemporalMinCount(
        arg,
        start_time=None,
        end_time=None,
        interval_type=None,
        interval_criterion=PostOperativePatients(),
        threshold=1,
    )


def PreOperativeBeforeDayOfSurgery(arg: logic.BaseExpr) -> logic.TemporalMinCount:
    """
    Applies a temporal constraint for the pre-operative period before the day of surgery.
    """
    return logic.TemporalMinCount(
        arg,
        start_time=None,
        end_time=None,
        interval_type=None,
        interval_criterion=PreOperativePatientsBeforeDayOfSurgery(),
        threshold=1,
    )


def PreOperativeBeforeSurgery(arg: logic.BaseExpr) -> logic.TemporalMinCount:
    """
    Applies a temporal constraint for the pre-operative period before the surgery.
    """
    return logic.TemporalMinCount(
        arg,
        start_time=None,
        end_time=None,
        interval_type=None,
        interval_criterion=PreOperativePatientsBeforeSurgery(),
        threshold=1,
    )


def OnFacesScaleAssessmentDayPostOp(arg: logic.BaseExpr) -> logic.TemporalMinCount:
    """
    Applies a post-operative constraint on the day of the Faces Anxiety Scale assessment.
    """
    return logic.TemporalMinCount(
        arg,
        start_time=None,
        end_time=None,
        interval_type=None,
        interval_criterion=And(
            PostOperativePatients(), OnFacesAnxietyScaleAssessmentDay()
        ),
        threshold=1,
    )


def PreFacesScalePostOp(arg: logic.BaseExpr) -> logic.TemporalMinCount:
    """
    Applies a post-operative constraint before the daily Faces Anxiety Scale assessment.
    """
    return logic.TemporalMinCount(
        arg,
        start_time=None,
        end_time=None,
        interval_type=None,
        interval_criterion=And(
            PostOperativePatients(), BeforeDailyFacesAnxietyScaleAssessment()
        ),
        threshold=1,
    )


def PreFacesScaleOnAssessmentDayPostOp(arg: logic.BaseExpr) -> logic.TemporalMinCount:
    """
    Applies a post-operative constraint for actions occurring before the daily Faces Anxiety Scale
    assessment on the day of that assessment.
    """
    return logic.TemporalMinCount(
        arg,
        start_time=None,
        end_time=None,
        interval_type=None,
        interval_criterion=And(
            PostOperativePatients(),
            OnFacesAnxietyScaleAssessmentDay(),
            BeforeDailyFacesAnxietyScaleAssessment(),
        ),
        threshold=1,
    )


dementia = ConditionOccurrence(
    static=False,
    value_required=False,
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
    value=None,
    timing=None,
)

vascularDementia = ConditionOccurrence(
    static=False,
    value_required=False,
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
    value=None,
    timing=None,
)

dementiaInOtherDiseases = ConditionOccurrence(
    static=False,
    value_required=False,
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
    value=None,
    timing=None,
)

dementiaInOtherDiseasesUnspecSeverity = ConditionOccurrence(
    static=False,
    value_required=False,
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
    value=None,
    timing=None,
)

dementiaUnspecified = ConditionOccurrence(
    static=False,
    value_required=False,
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
    value=None,
    timing=None,
)

anyDementiaBeforeDayOfSurgery = Or(
    PreOperativeBeforeDayOfSurgery(dementia),
    PreOperativeBeforeDayOfSurgery(vascularDementia),
    PreOperativeBeforeDayOfSurgery(dementiaInOtherDiseases),
    PreOperativeBeforeDayOfSurgery(dementiaInOtherDiseasesUnspecSeverity),
    PreOperativeBeforeDayOfSurgery(dementiaUnspecified),
)

anyDementiaBeforeSurgery = Or(
    PreOperativeBeforeSurgery(dementia),
    PreOperativeBeforeSurgery(vascularDementia),
    PreOperativeBeforeSurgery(dementiaInOtherDiseases),
    PreOperativeBeforeSurgery(dementiaInOtherDiseasesUnspecSeverity),
    PreOperativeBeforeSurgery(dementiaUnspecified),
)


asaGTe2 = Measurement(
    static=False,
    value_required=True,
    concept=Concept(
        concept_id=4199571,
        concept_name="American Society of Anesthesiologists physical status class",
        concept_code="302132005",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
    timing=None,
)

cciGte2 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.RESULT_OF_CHARLSON_COMORBIDITY_INDEX,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
    timing=None,
)

minicogLt3 = Measurement(
    static=False,
    value_required=True,
    concept=Concept(
        concept_id=37017178,
        concept_name="Mini-Cog test score",
        concept_code="713408000",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept=None,
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
    timing=None,
)

mmseLt25 = Measurement(
    static=False,
    value_required=True,
    concept=Concept(
        concept_id=40491929,
        concept_name="Mini-mental state examination score",
        concept_code="447316007",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept=None,
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=24.99975),
    timing=None,
)

acerLt88 = Measurement(
    static=False,
    value_required=True,
    concept=Concept(
        concept_id=44804259,
        concept_name="Addenbrooke's cognitive examination revised - score",
        concept_code="711061000000109",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept=None,
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=87.99912),
    timing=None,
)

mocaLt26 = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=43054915,
        concept_name="Total score [MoCA]",
        concept_code="72172-0",
        domain_id="Observation",
        vocabulary_id="LOINC",
        concept_class_id="Survey",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=25.99974),
    timing=None,
)

anyCognitiveImpairmentBeforeDayOfSurgery = Or(
    PreOperativeBeforeDayOfSurgery(AgeLimitPatient(min_age_years=70)),
    PreOperativeBeforeDayOfSurgery(asaGTe2),
    PreOperativeBeforeDayOfSurgery(cciGte2),
    PreOperativeBeforeDayOfSurgery(minicogLt3),
    PreOperativeBeforeDayOfSurgery(mmseLt25),
    PreOperativeBeforeDayOfSurgery(acerLt88),
    PreOperativeBeforeDayOfSurgery(mocaLt26),
)

facesAnxietyScoreAssessed = Measurement(
    static=False,
    value_required=False,
    concept=custom_concepts.FACES_ANXIETY_SCALE_SCORE,
    forward_fill=False,
    value=None,
    # timing=Timing(
    #     count={"unit": None, "value": None, "value_min": 1, "value_max": None},
    #     duration=None,
    #     frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
    #     interval={
    #         "unit": TimeUnit.DAY,
    #         "value": 1,
    #         "value_min": None,
    #         "value_max": None,
    #     },
    # ),
)

nuDescGte2 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
    timing=None,
)

nudescLt2 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=1.99998),
    timing=None,
)

nuDescPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

nudescNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

nudescWeaklyPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4127785,
            "concept_name": "Weakly positive",
            "concept_code": "260408008",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

icdscGte4 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
    timing=None,
)

icdscPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

icdscLt4 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=3.99996),
    timing=None,
)

icdscNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

icdscWeaklyPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4127785,
            "concept_name": "Weakly positive",
            "concept_code": "260408008",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

camPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.CONFUSION_ASSESSMENT_METHOD_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

camNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.CONFUSION_ASSESSMENT_METHOD_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

drsGte12 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_RATING_SCALE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=12.0, value_max=None),
    timing=None,
)

drsPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_RATING_SCALE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

drsLt12 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_RATING_SCALE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=11.99988),
    timing=None,
)

drsNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_RATING_SCALE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

drsWeaklyPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_RATING_SCALE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4127785,
            "concept_name": "Weakly positive",
            "concept_code": "260408008",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

dosGte3 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_OBSERVATION_SCALE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=3.0, value_max=None),
    timing=None,
)

dosPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_OBSERVATION_SCALE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

dosLt3 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_OBSERVATION_SCALE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=2.99997),
    timing=None,
)

dosNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_OBSERVATION_SCALE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

dosWeaklyPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_OBSERVATION_SCALE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4127785,
            "concept_name": "Weakly positive",
            "concept_code": "260408008",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

tdcamPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.THREE_MINUTE_DIAGNOSTIC_INTERVIEW_FOR_CAM_DEFINED_DELIRIUM_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

tdcamNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.THREE_MINUTE_DIAGNOSTIC_INTERVIEW_FOR_CAM_DEFINED_DELIRIUM_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)


camicuPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.CONFUSION_ASSESSMENT_METHOD_FOR_THE_INTENSIVE_CARE_UNIT_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

camicuNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.CONFUSION_ASSESSMENT_METHOD_FOR_THE_INTENSIVE_CARE_UNIT_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

ddsGte7 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_DETECTION_SCORE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=7.0, value_max=None),
    timing=None,
)

ddsLt8 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_DETECTION_SCORE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=7.99992),
    timing=None,
)

ddsPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_DETECTION_SCORE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

ddsNegative = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_DETECTION_SCORE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

ddsWeaklyPositive = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.DELIRIUM_DETECTION_SCORE_SCORE,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4127785,
            "concept_name": "Weakly positive",
            "concept_code": "260408008",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

FourAtGte4 = Measurement(
    static=False,
    value_required=True,
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
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=4.0, value_max=None),
    timing=None,
)

FourAtLt4 = Measurement(
    static=False,
    value_required=True,
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
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=None, value_max=3.99996),
    timing=None,
)

FourAtPositive = Measurement(
    static=False,
    value_required=True,
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
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9191,
            "concept_name": "Positive",
            "concept_code": "10828004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

FourAtNegative = Measurement(
    static=False,
    value_required=True,
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
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 9189,
            "concept_name": "Negative",
            "concept_code": "260385009",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

FourAtWeaklyPositive = Measurement(
    static=False,
    value_required=True,
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
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4127785,
            "concept_name": "Weakly positive",
            "concept_code": "260408008",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)


anyPositiveDeliriumTest = Or(
    PostOperative(nuDescGte2),
    PostOperative(nuDescPositive),
    PostOperative(icdscGte4),
    PostOperative(icdscPositive),
    PostOperative(camPositive),
    PostOperative(drsGte12),
    PostOperative(drsPositive),
    PostOperative(dosGte3),
    PostOperative(dosPositive),
    PostOperative(tdcamPositive),
    PostOperative(camicuPositive),
    PostOperative(ddsGte7),
    PostOperative(ddsPositive),
    PostOperative(FourAtGte4),
    PostOperative(FourAtPositive),
)

facesAnxietyScoreGte2 = Measurement(
    static=False,
    value_required=True,
    concept=custom_concepts.FACES_ANXIETY_SCALE_SCORE,
    forward_fill=True,
    value=ValueScalar(unit=None, value=None, value_min=2.0, value_max=None),
    timing=None,
)


nonPharmaAnxietyIntervention = ProcedureOccurrence(
    static=False,
    timing=None,
    concept=custom_concepts.NON_PHARMACOLOGICAL_INTERVENTION_FOR_ANXIETY_MANAGEMENT,
    value=None,
)

verbalAnxietyManagement = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.VERBAL_MANAGEMENT_OF_ANXIETY,
    value=None,
)

triggerAvoidanceForAnxiety = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.AVOIDANCE_OF_TRIGGER_FACTORS_FOR_ANXIETY,
    value=None,
)

socialServiceInterview = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4131661,
        concept_name="Social service interview of patient",
        concept_code="2658000",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

palliativeCareConsultation = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=37018932,
        concept_name="Consultation for palliative care",
        concept_code="713281006",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

familyInvolvementInCare = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4021023,
        concept_name="Involving family and friends in care",
        concept_code="225329001",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

individualizedPatientEducation = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4187602,
        concept_name="Patient education based on identified need",
        concept_code="372919008",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

identificationOfCarePreferences = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4158828,
        concept_name="Identification of individual values and wishes concerning care",
        concept_code="370819000",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

cognitiveStimulationProcedure = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4301075,
        concept_name="Cognitive stimulation",
        concept_code="386241007",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

readingActivity = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.READING_OR_READING_TO_SOMEBODY,
    value=None,
)

conversationForCognition = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.CONVERSATION_TO_STIMULATE_COGNITION,
    value=None,
)

boardGamesOrPuzzles = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.PLAYING_BOARD_GAMES_OR_PUZZLES,
    value=None,
)

singingActivity = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.SINGING,
    value=None,
)

cognitiveAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4012466,
        concept_name="Assessment and interpretation of higher cerebral function, cognitive testing",
        concept_code="113024001",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

communicationAidProvision = ProcedureOccurrence(
    static=False,
    timing=None,
    concept=Concept(
        concept_id=4043216,
        concept_name="Provision of communication aid",
        concept_code="228620008",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

spectacleSupply = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4322820,
        concept_name="Supply of spectacles",
        concept_code="7128000",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

hearingAidProvision = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4085698,
        concept_name="Hearing aid provision",
        concept_code="281656009",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

assistiveWritingDevice = DeviceExposure(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=45763977,
        concept_name="Assistive writing/drafting/drawing board",
        concept_code="700540009",
        domain_id="Device",
        vocabulary_id="SNOMED",
        concept_class_id="Physical Object",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

removableDentureProvision = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4082890,
        concept_name="Provision of removable denture",
        concept_code="183117009",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

interpreterServiceRequest = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=40482038,
        concept_name="Request for language interpreter service",
        concept_code="445075008",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

communicationAssistiveDevice = DeviceExposure(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=45771498,
        concept_name="Communication and information assistive device",
        concept_code="705371001",
        domain_id="Device",
        vocabulary_id="SNOMED",
        concept_class_id="Physical Object",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

supportCircadianRhythm = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.NON_PHARMACOLOGICAL_INTERVENTION_TO_SUPPORT_THE_CIRCADIAN_RHYTHM,
    value=None,
)

sleepingMaskProvision = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.PROVISION_OF_SLEEPING_MASK,
    value=None,
)

earplugsAtNight = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.PROVISION_OF_EARPLUGS_AT_NIGHT,
    value=None,
)

noiseReduction = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.REDUCTION_OF_NOISE,
    value=None,
)

lightExposureDaytime = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.LIGHT_EXPOSURE_DURING_DAYTIME,
    value=None,
)

reduceNightLight = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.REDUCTION_OF_LIGHT_EXPOSURE_AT_NIGHTTIME,
    value=None,
)

closePatientRoomDoor = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.CLOSING_THE_DOOR_OF_THE_PATIENT_ROOM,
    value=None,
)

promoteSleepHygiene = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=37156352,
        concept_name="Promotion of sleep hygiene",
        concept_code="1172583004",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

onlyEmergencyAtNight = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.PERFORMS_ONLY_EMERGENCY_PROCEDURES_AT_NIGHTTIME,
    value=None,
)

otherSleepHygieneInterventions = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=custom_concepts.OTHER_NON_PHARMACOLOGICAL_INTERVENTIONS_TO_PROMOTE_SLEEP_HYGIENE,
    value=None,
)

realityOrientation = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4038867,
        concept_name="Reality orientation",
        concept_code="228547007",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

wearableWatch = DeviceExposure(
    static=False,
    value_required=False,
    concept=custom_concepts.WATCH,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

calendarDevice = DeviceExposure(
    static=False,
    value_required=False,
    concept=custom_concepts.CALENDAR,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

printedMaterial = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4081701,
        concept_name="Printed material",
        concept_code="278211009",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Physical Object",
        standard_concept=None,
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

televisionDevice = DeviceExposure(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4114817,
        concept_name="Television",
        concept_code="255712000",
        domain_id="Device",
        vocabulary_id="SNOMED",
        concept_class_id="Physical Object",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

radioDevice = DeviceExposure(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4234434,
        concept_name="Radio",
        concept_code="360004001",
        domain_id="Device",
        vocabulary_id="SNOMED",
        concept_class_id="Physical Object",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

otherMediaExposure = DeviceExposure(
    static=False,
    value_required=False,
    concept=custom_concepts.OTHER_MEDIA,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

mobilizationAbilityObservation = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4103497,
        concept_name="Ability to mobilize",
        concept_code="301438001",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

physiatricJointMobilization = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4251052,
        concept_name="Physiatric mobilization of joint",
        concept_code="74251004",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

contraindicationObservation = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4141768,
        concept_name="Medical contraindication to procedure",
        concept_code="266757004",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Context-dependent",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

patientNonCompliance = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4136190,
        concept_name="Patient non-compliant - declined intervention / support",
        concept_code="413311005",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Context-dependent",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

lackOfEnergyCondition = ConditionOccurrence(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4087481,
        concept_name="Lack of energy",
        concept_code="248274002",
        domain_id="Condition",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

anxietyCondition = ConditionOccurrence(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=441542,
        concept_name="Anxiety",
        concept_code="48694002",
        domain_id="Condition",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

painCondition = ConditionOccurrence(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4329041,
        concept_name="Pain",
        concept_code="22253000",
        domain_id="Condition",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

exhaustionObservation = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4246495,
        concept_name="Exhaustion",
        concept_code="60119000",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

dizzinessCondition = ConditionOccurrence(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4223938,
        concept_name="Dizziness",
        concept_code="404640003",
        domain_id="Condition",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

reasonAndJustificationObservation = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4128496,
        concept_name="Reason and justification",
        concept_code="288830005",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Attribute",
        standard_concept=None,
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)
##############################
selfFeedingAbility = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4128668,
        concept_name="Ability to feed self",
        concept_code="288999009",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

enteralFeeding = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4042005,
        concept_name="Enteral feeding",
        concept_code="229912004",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

ivFeeding = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4096831,
        concept_name="Intravenous feeding of patient",
        concept_code="25156005",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

aspirationRisk = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4160501,
        concept_name="At increased risk for aspiration",
        concept_code="371736008",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

abnormalDeglutition = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4166234,
        concept_name="Abnormal deglutition",
        concept_code="47717004",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)


lossOfAppetite = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=442165,
        concept_name="Loss of appetite",
        concept_code="79890006",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

digestiveReflux = ConditionOccurrence(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=46271381,
        concept_name="Digestive system reflux",
        concept_code="709493000",
        domain_id="Condition",
        vocabulary_id="SNOMED",
        concept_class_id="Clinical Finding",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

nauseaAndVomiting = ConditionOccurrence(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=27674,
        concept_name="Nausea and vomiting",
        concept_code="16932000",
        domain_id="Condition",
        vocabulary_id="SNOMED",
        concept_class_id="Disorder",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

deglutitionMeasurement = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4185237,
        concept_name="Deglutition",
        concept_code="54731003",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4166234,
            "concept_name": "Abnormal deglutition",
            "concept_code": "47717004",
            "domain_id": "Observation",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Clinical Finding",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

dysphagiaTherapy = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=4210275,
        concept_name="Dysphagia therapy regime",
        concept_code="311569007",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

nutritionalRegimeModification = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
    concept=Concept(
        concept_id=763733,
        concept_name="Modification of nutritional regime",
        concept_code="445341000124100",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

mouthCare = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=37397340,
        concept_name="Mouth care",
        concept_code="717778001",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

deglutition = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4185237,
        concept_name="Deglutition",
        concept_code="54731003",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency={"unit": None, "value": None, "value_min": 1, "value_max": None},
        interval={
            "unit": TimeUnit.DAY,
            "value": 1,
            "value_min": None,
            "value_max": None,
        },
    ),
)

selfFeeding = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4128668,
        concept_name="Ability to feed self",
        concept_code="288999009",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4122440,
            "concept_name": "Does not feed self",
            "concept_code": "289003008",
            "domain_id": "Observation",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Clinical Finding",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

mobility = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4103497,
        concept_name="Ability to mobilize",
        concept_code="301438001",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Observable Entity",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4200193,
            "concept_name": "Does not mobilize",
            "concept_code": "302045007",
            "domain_id": "Observation",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Clinical Finding",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)
