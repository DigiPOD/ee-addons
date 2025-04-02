from execution_engine.omop.concepts import Concept

from digipod.terminology.vocabulary import (  # BRADYCARDIA_DURING_SURGERY as Bradycardia_During_Surgery; noqa: we expose these concepts intentionally
    CONFUSION_ASSESSMENT_METHOD_FOR_THE_INTENSIVE_CARE_UNIT_SCORE,
    CONFUSION_ASSESSMENT_METHOD_SCORE,
    DELIRIUM_DETECTION_SCORE_SCORE,
    DELIRIUM_OBSERVATION_SCALE_SCORE,
    DELIRIUM_RATING_SCALE_SCORE,
    INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    THREE_MINUTE_DIAGNOSTIC_INTERVIEW_FOR_CAM_DEFINED_DELIRIUM_SCORE,
    DigiPOD,
)

OMOP_INTENSIVE_CARE = 32037
OMOP_INPATIENT_VISIT = 9201
OMOP_OUTPATIENT_VISIT = 9202
OMOP_MMSE = 40491929
OMOP_ASA = 4199571
OMOP_MINICOG = 37017178
OMOP_MOCA = 37174522
OMOP_RASS = 36684829
OMOP_4AT = 3662219
OMOP_DEMENTIA = 4182210
OMOP_ASSESSMENT_OF_DELIRIUM = 37116854
OMOP_RISK_ASSESSMENT_DONE = 37018976
OMOP_POSITIVE = 9191
OMOP_NOT_PERFORMED = 4118638
OMOP_DEXMEDETOMIDINE = 19061088
OMOP_BASELINE_BRADYCARDIA = 4082927
OMOP_LOW_BLOOD_PRESSURE = 317002
OMOP_DRUG_INDUCED_BRADYCARDIA = 4262316
OMOP_DRUG_INDUCED_HYPOTENSION = 4120275
OMOP_HYPOTENSION_DURING_SURGERY = 37108683

SCT_SUBSTANCE = "105590001"

# Gender
OMOP_GENDER_FEMALE = 8532
OMOP_GENDER_MALE = 8507

IntensiveCare = Concept(
    concept_id=OMOP_INTENSIVE_CARE,
    concept_name="Intensive Care",
    concept_code="Intensive Care",
    domain_id="Visit",
    vocabulary_id="Custom",
    concept_class_id="Custom",
)

InpatientVisit = Concept(
    concept_id=OMOP_INPATIENT_VISIT,
    concept_name="Inpatient Visit",
    concept_code="Inpatient Visit",
    domain_id="Visit",
    vocabulary_id="Custom",
    concept_class_id="Custom",
)

OutpatientVisit = Concept(
    concept_id=OMOP_OUTPATIENT_VISIT,
    concept_name="Outpatient Visit",
    concept_code="Outpatient Visit",
    domain_id="Visit",
    vocabulary_id="Custom",
    concept_class_id="Custom",
)

MMSE = Concept(
    concept_id=OMOP_MMSE,
    concept_name="Mini-mental state examination score",
    concept_code="447316007",
    domain_id="Measurement",
    vocabulary_id="SNOMED",
    concept_class_id="Observable Entity",
)


unit_score = Concept(
    concept_id=44777566,
    concept_name="score",
    concept_code="score",
    domain_id="Unit",
    vocabulary_id="UCUM",
    concept_class_id="Unit",
)


RASS = Concept(
    concept_id=OMOP_RASS,
    concept_name="Richmond Agitation-Sedation Scale",
    concept_code="457441000124102",
    domain_id="Measurement",
    vocabulary_id="SNOMED",
    concept_class_id="Staging / Scales",
)


FourAT = Concept(
    concept_id=OMOP_4AT,
    concept_name="4AT - 4 A's Test",
    concept_code="1239191000000102",
    domain_id="Measurement",
    vocabulary_id="SNOMED",
    concept_class_id="Staging / Scales",
)

Dementia = Concept(
    concept_id=OMOP_DEMENTIA,
    concept_name="Dementia",
    concept_code="52448006",
    domain_id="Condition",
    vocabulary_id="SNOMED",
    concept_class_id="Disorder",
)

AssessmentOfDelirium = Concept(
    concept_id=OMOP_ASSESSMENT_OF_DELIRIUM,
    concept_name="Assessment of delirium",
    concept_code="733870009",
    domain_id="Procedure",
    vocabulary_id="SNOMED",
    concept_class_id="Procedure",
)

RiskAssessmentDone = Concept(
    concept_id=OMOP_RISK_ASSESSMENT_DONE,
    concept_name="Procedure",
    concept_code="712741005",
    domain_id="Observation",
    vocabulary_id="SNOMED",
    concept_class_id="Context-dependent",
)

Positive = Concept(
    concept_id=OMOP_POSITIVE,
    concept_name="Positive",
    concept_code="10828004",
    domain_id="Measurement",
    vocabulary_id="SNOMED",
    concept_class_id="Qualifier Value",
)

NotPerformed = Concept(
    concept_id=OMOP_NOT_PERFORMED,
    concept_name="Not performed",
    concept_code="262008008",
    domain_id="Measurement",
    vocabulary_id="SNOMED",
    concept_class_id="Qualifier Value",
)

Dexmedetomidine = Concept(
    concept_id=OMOP_DEXMEDETOMIDINE,
    concept_name="dexmedetomidine",
    concept_code="48937",
    domain_id="Drug",
    vocabulary_id="RxNorm",
    concept_class_id="Ingredient",
)

# Before Dexmedetomidine started
Baseline_Bradycardia = Concept(
    concept_id=OMOP_BASELINE_BRADYCARDIA,
    concept_name="Baseline bradycardia",
    concept_code="278085001",
    domain_id="Condition",
    vocabulary_id="SNOMED",
    concept_class_id="Clinical Finding",
)

Low_Blood_Pressure = Concept(
    concept_id=OMOP_LOW_BLOOD_PRESSURE,
    concept_name="Low blood pressure",
    concept_code="45007003",
    domain_id="Condition",
    vocabulary_id="SNOMED",
    concept_class_id="Disorder",
)

# After Dexmedetomidine started
Drug_Induced_Bradycardia = Concept(
    concept_id=OMOP_DRUG_INDUCED_BRADYCARDIA,
    concept_name="Drug-induced bradycardia",
    concept_code="397841007",
    domain_id="Condition",
    vocabulary_id="SNOMED",
    concept_class_id="Disorder",
)

Drug_Induced_Hypotension = Concept(
    concept_id=OMOP_DRUG_INDUCED_HYPOTENSION,
    concept_name="Drug-induced hypotension",
    concept_code="234171009",
    domain_id="Condition",
    vocabulary_id="SNOMED",
    concept_class_id="Disorder",
)

# During surgery

Hypotension_During_Surgery = Concept(
    concept_id=OMOP_HYPOTENSION_DURING_SURGERY,
    concept_name="Hypotension during surgery",
    concept_code="10901000087102",
    domain_id="Condition",
    vocabulary_id="SNOMED",
    concept_class_id="Disorder",
)
