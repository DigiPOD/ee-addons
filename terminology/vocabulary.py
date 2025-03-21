from execution_engine.omop.concepts import Concept
from execution_engine.omop.vocabulary import (
    LOINC,
    SNOMEDCT,
    AbstractVocabulary,
    standard_vocabulary,
)

from .custom_concepts import *

# DIGIPOD_CONCEPT_OFFSET = 2000000000
# UNMAPPED_CONCEPT_ID = DIGIPOD_CONCEPT_OFFSET + 99999999


# vocab_id = "DIGIPOD"

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

# as of 25-03-10 this SNOMEDCT concept hasn't been integrated into the OMOP standard vocabulary
# hence, we define it ourselves with a custom concept code.
CAM = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 13,
    concept_name="Confusion Assessment Method score (observable entity)",
    concept_code="1351493007",
    domain_id="Measurement",
    vocabulary_id=SNOMEDCT.omop_vocab_name,
    concept_class_id="Custom",
)

# as of 25-03-10 this SNOMEDCT concept hasn't been integrated into the OMOP standard vocabulary
# hence, we define it ourselves with a custom concept code.
ICDSC = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 18,
    concept_name="Intensive Care Delirium Screening Checklist score (observable entity)",
    concept_code="1351995008",
    domain_id="Measurement",
    vocabulary_id=SNOMEDCT.omop_vocab_name,
    concept_class_id="Custom",
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
