from execution_engine.omop.concepts import Concept

OMOP_INTENSIVE_CARE = 32037
OMOP_INPATIENT_VISIT = 9201
OMOP_OUTPATIENT_VISIT = 9202
OMOP_SURGICAL_PROCEDURE = 4301351  # OMOP surgical procedure
OMOP_MMSE = 40491929
OMOP_ASA = 4199571
OMOP_MINICOG = 37017178
OMOP_MOCA = 37174522
OMOP_RASS = 36684829

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
