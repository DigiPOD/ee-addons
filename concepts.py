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
