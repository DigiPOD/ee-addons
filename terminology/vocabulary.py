from execution_engine.omop.concepts import Concept
from execution_engine.omop.vocabulary import AbstractVocabulary

DIGIPOD_CONCEPT_OFFSET = 2000000000

vocab_id = "DIGIPOD"


CHARLSON_COMORBIDITY_INDEX = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 3,
    concept_name="Result of Charlson Comorbidity Index",
    concept_code="009",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

DATE_OF_SURGICAL_PROCEDURE = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 7,
    concept_name="Date of surgical procedure",
    concept_code="007",
    domain_id="Event",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

NuDESC = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 12,
    concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
    concept_code="016",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

CAM = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 13,
    concept_name="Confusion Assessment Method score",
    concept_code="018",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

ThreeDCAM = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 14,
    concept_name="3-minute Diagnostic Interview for CAM-defined Delirium score",
    concept_code="021",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

DRS = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 15,
    concept_name="Delirium Rating Scale score",
    concept_code="019",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

DOS = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 16,
    concept_name="Delirium Observation Scale score",
    concept_code="020",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

CAM_ICU = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 17,
    concept_name="Confusion Assessment Method for the Intensive Care Unit score",
    concept_code="022",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

ICDSC = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 18,
    concept_name="Intensive Care Delirium Screening Checklist score",
    concept_code="024",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

DDS = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 19,
    concept_name="Delirium Detection Score score",
    concept_code="023",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

ADDENBROOKE_COGNITIVE_EXAMINATION = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 100012,
    concept_name="Result of Addenbrooke cognitive examination revised",
    concept_code="012",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)


class DigiPOD(AbstractVocabulary):
    """
    DigiPOD vocabulary.
    """

    system_uri = "https://www.charite.de/fhir/digipod/CodeSystem/digipod"

    map = {
        "007": DATE_OF_SURGICAL_PROCEDURE,
        "009": CHARLSON_COMORBIDITY_INDEX,
        "012": ADDENBROOKE_COGNITIVE_EXAMINATION,
        "016": NuDESC,
        "018": CAM,
        "019": DRS,
        "020": DOS,
        "021": ThreeDCAM,
        "022": CAM_ICU,
        "023": DDS,
        "024": ICDSC,
    }

    @classmethod
    def omop_concept(cls, concept: str, standard: bool = False) -> Concept:
        """
        Get the OMOP Standard Vocabulary standard concept for the given code in the given vocabulary.
        """

        if concept not in cls.map:
            raise KeyError(
                f"Concept {concept} not found in {cls.system_uri} vocabulary"
            )

        return cls.map[concept]
