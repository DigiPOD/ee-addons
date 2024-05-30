from execution_engine.omop.concepts import Concept, CustomConcept
from execution_engine.omop.vocabulary import AbstractVocabulary


class DigiPOD(AbstractVocabulary):
    """
    DigiPOD vocabulary.
    """

    system_uri = "https://www.charite.de/fhir/digipod/CodeSystem/digipod"
    vocab_id = "DIGIPOD"
    map = {
        "009": CustomConcept(
            name="Result of Charlson Comorbidity Index",
            concept_code="009",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
        ),
        "016": CustomConcept(
            name="Nursing Delirium Screening Scale (NU-DESC) score",
            concept_code="016",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
        ),
        "017": CustomConcept(
            name="4AT score",
            concept_code="017",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
        ),
        "018": CustomConcept(
            name="Confusion Assessment Method score",
            concept_code="018",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
        ),
        "019": CustomConcept(
            name="Delirium Rating Scale score",
            concept_code="019",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
        ),
        "020": CustomConcept(
            name="Delirium Observation Scale score",
            concept_code="020",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
        ),
        "021": CustomConcept(
            name="3-minute Diagnostic Interview for CAM-defined Delirium score",
            concept_code="021",
            domain_id="Measurement",
            vocabulary_id=vocab_id,
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
