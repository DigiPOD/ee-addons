from execution_engine.omop.concepts import Concept
from execution_engine.omop.vocabulary import AbstractVocabulary

DIGIPOD_CONCEPT_OFFSET = 2000000000


class DigiPOD(AbstractVocabulary):
    """
    DigiPOD vocabulary.
    """

    system_uri = "https://www.charite.de/fhir/digipod/CodeSystem/digipod"
    vocab_id = "DIGIPOD"
    map = {
        "007": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 7,
            concept_name="Date of surgical procedure",
            concept_code="007",
            domain_id="Event",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "009": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 9,
            concept_name="Result of Charlson Comorbidity Index",
            concept_code="009",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "012": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 12,
            concept_name="Result of Addenbrooke cognitive examination revised",
            concept_code="012",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "016": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 16,
            concept_name="Nursing Delirium Screening Scale (NU-DESC) score",
            concept_code="016",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "017": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 17,
            concept_name="4AT score",
            concept_code="017",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "018": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 18,
            concept_name="Confusion Assessment Method score",
            concept_code="018",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "019": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 19,
            concept_name="Delirium Rating Scale score",
            concept_code="019",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "020": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 20,
            concept_name="Delirium Observation Scale score",
            concept_code="020",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "021": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 21,
            concept_name="3-minute Diagnostic Interview for CAM-defined Delirium score",
            concept_code="021",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "022": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 22,
            concept_name="Confusion Assessment Method for the Intensive Care Unit score",
            concept_code="022",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "023": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 23,
            concept_name="Delirium Detection Score score",
            concept_code="023",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
        "024": Concept(
            concept_id=DIGIPOD_CONCEPT_OFFSET + 24,
            concept_name="Intensive Care Delirium Screening Checklist score",
            concept_code="024",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
            concept_class_id="Custom",
        ),
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
