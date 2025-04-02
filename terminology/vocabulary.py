from execution_engine.omop.concepts import Concept
from execution_engine.omop.vocabulary import (
    LOINC,
    SNOMEDCT,
    AbstractVocabulary,
    standard_vocabulary,
)

from .custom_concepts import *

# $sct-uk#711061000000109 "Addenbrooke's cognitive examination revised - score (observable entity)"
ACE_R = standard_vocabulary.get_concept(
    SNOMEDCT.system_uri, "711061000000109", standard=False
)

# $sct#1255891005 "Montreal Cognitive Assessment version 8.1 score (observable entity)"
MOCA = standard_vocabulary.get_concept(SNOMEDCT.system_uri, "1255891005")

# $loinc#72172-0 "Total score [MoCA]"
MOCA_LOINC = standard_vocabulary.get_concept(LOINC.system_uri, "72172-0")

# $sct#302132005 "American Society of Anesthesiologists physical status class (observable entity)"
ASA = standard_vocabulary.get_concept(SNOMEDCT.system_uri, "302132005")

# $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
MINICOG = standard_vocabulary.get_concept(
    SNOMEDCT.system_uri, "713408000", standard=False
)


class DigiPOD(AbstractVocabulary):
    """
    DigiPOD vocabulary.
    """

    system_uri = "https://www.charite.de/fhir/digipod/CodeSystem/digipod"

    map: dict[str, Concept] = {}  # created automatically (see below)

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


DigiPOD.map = {
    obj.concept_code: obj
    for name, obj in globals().items()
    if isinstance(obj, Concept)
    and hasattr(obj, "concept_code")
    and getattr(obj, "vocabulary_id") == vocab_id
}
