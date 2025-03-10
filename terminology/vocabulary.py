from execution_engine.omop.concepts import Concept
from execution_engine.omop.vocabulary import SNOMEDCT, AbstractVocabulary

DIGIPOD_CONCEPT_OFFSET = 2000000000
UNMAPPED_CONCEPT_ID = DIGIPOD_CONCEPT_OFFSET + 99999999

vocab_id = "DIGIPOD"

OPTIMIZABLE_RISK_FACTOR = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 4,
    concept_name="Presence of optimizable preoperative risk factor",
    concept_code="007",
    domain_id="Observation",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

PREOPERATIVE_RISK_FACTOR_OPTIMIZATION = Concept(
    concept_id=UNMAPPED_CONCEPT_ID,
    concept_name="Preoperative risk factor optimization",
    concept_code="008",
    domain_id="Procedure",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

CHARLSON_COMORBIDITY_INDEX = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 3,
    concept_name="Result of Charlson Comorbidity Index",
    concept_code="009",
    domain_id="Measurement",
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

ASSESSMENT_OF_POSTOPERATIVE_DELIRIUM = Concept(
    concept_id=UNMAPPED_CONCEPT_ID,
    concept_name="Assessment for risk of post-operative delirium",
    concept_code="017",
    domain_id="Procedure",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
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

ThreeDCAM = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 14,
    concept_name="3-minute Diagnostic Interview for CAM-defined Delirium score",
    concept_code="021",
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

DDS = Concept(
    concept_id=DIGIPOD_CONCEPT_OFFSET + 19,
    concept_name="Delirium Detection Score score",
    concept_code="023",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
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

# BRADYCARDIA_DURING_SURGERY = Concept(
#     concept_id=DIGIPOD_CONCEPT_OFFSET + 31,
#     concept_name="Bradycardia During Surgery",
#     concept_code="031",
#     domain_id="Condition",
#     vocabulary_id=vocab_id,
#     concept_class_id="Custom",
# )

COMPLETION_TIME_OF_SURGICAL_PROCEDURE = Concept(
    concept_id=UNMAPPED_CONCEPT_ID,
    concept_name="Completion time of surgical procedure",
    concept_code="034",
    domain_id="Measurement",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

BEFORE_DEXMEDETOMIDINE_ADMINISTRATION = Concept(
    concept_id=UNMAPPED_CONCEPT_ID,
    concept_name="Before dexmedetomidine administration",
    concept_code="029",
    domain_id="Observation",
    vocabulary_id=vocab_id,
    concept_class_id="Custom",
)

ADMINISTRATION_OF_PROPHYLACTIC_DEXMEDETOMIDINE = Concept(
    concept_id=UNMAPPED_CONCEPT_ID,
    concept_name="Administration of prophylactic dexmedetomidine",
    concept_code="024",
    domain_id="Observation",
    vocabulary_id=vocab_id,
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
    if isinstance(obj, Concept) and hasattr(obj, "concept_code")
}
