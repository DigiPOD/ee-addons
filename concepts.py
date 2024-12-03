from execution_engine.omop.concepts import Concept

INTENSIVE_CARE = 32037
INPATIENT_VISIT = 9201
OUTPATIENT_VISIT = 9202

IntensiveCare = Concept(
    concept_id=INTENSIVE_CARE,
    concept_name="Intensive Care",
    concept_code="Intensive Care",
    domain_id="Visit",
    vocabulary_id="Custom",
    concept_class_id="Custom",
)

InpatientVisit = Concept(
    concept_id=INPATIENT_VISIT,
    concept_name="Inpatient Visit",
    concept_code="Inpatient Visit",
    domain_id="Visit",
    vocabulary_id="Custom",
    concept_class_id="Custom",
)

OutpatientVisit = Concept(
    concept_id=OUTPATIENT_VISIT,
    concept_name="Outpatient Visit",
    concept_code="Outpatient Visit",
    domain_id="Visit",
    vocabulary_id="Custom",
    concept_class_id="Custom",
)

MMSE = Concept(
    concept_id=40491929,
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
    concept_id=36684829,
    concept_name="Richmond Agitation-Sedation Scale",
    concept_code="457441000124102",
    domain_id="Measurement",
    vocabulary_id="SNOMED",
    concept_class_id="Staging / Scales",
)
