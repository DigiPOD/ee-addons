from typing import Type, TypedDict

from execution_engine.converter.characteristic.abstract import AbstractCharacteristic
from execution_engine.converter.characteristic.value import AbstractValueCharacteristic
from execution_engine.converter.criterion import parse_code, parse_value
from execution_engine.fhir.util import get_coding
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.concept import ConceptCriterion
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.vocabulary import LOINC, SNOMEDCT, AbstractVocabulary
from execution_engine.util import logic
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic

from digipod.concepts import MMSE
from digipod.terminology.vocabulary import (
    ACE_R,
    ASA,
    CONFUSION_ASSESSMENT_METHOD_FOR_THE_INTENSIVE_CARE_UNIT_SCORE,
    CONFUSION_ASSESSMENT_METHOD_SCORE,
    DELIRIUM_DETECTION_SCORE_SCORE,
    DELIRIUM_OBSERVATION_SCALE_SCORE,
    DELIRIUM_RATING_SCALE_SCORE,
    FACES_ANXIETY_SCALE_SCORE,
    INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    MINICOG,
    MOCA,
    MOCA_LOINC,
    NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    OPTIMIZABLE_PREOPERATIVE_RISK_FACTOR,
    RESULT_OF_CHARLSON_COMORBIDITY_INDEX,
    THREE_MINUTE_DIAGNOSTIC_INTERVIEW_FOR_CAM_DEFINED_DELIRIUM_SCORE,
    DigiPOD,
)


class ConceptEntry(TypedDict, total=False):
    """
    Represents a concept entry with a code, vocabulary, and an optional replacement.

    :param code: The concept code.
    :param vocabulary: The vocabulary associated with the concept.
    :param replace: (Optional) A replacement concept if applicable.
    """

    code: str
    vocabulary: Type[AbstractVocabulary]
    replace: Concept


class ObservationCharacteristicConverter(AbstractValueCharacteristic):
    """
    Converts Observations (from DigiPOD Vocabulary)
    """

    _concepts: list[ConceptEntry] = [
        # Nursing Delirium Screening Scale (NU-DESC) score
        {
            "code": NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE.concept_code,
            "vocabulary": DigiPOD,
        },
        # Intensive Care Delirium Screening Checklist score (observable entity)
        {
            "code": "1351995008",
            "vocabulary": SNOMEDCT,
            "replace": INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
        },
        # Intensive Care Delirium Screening Checklist score (observable entity)
        {
            "code": INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE.concept_code,
            "vocabulary": DigiPOD,
        },
        # Confusion Assessment Method score (observable entity)
        {
            "code": "1351493007",
            "vocabulary": SNOMEDCT,
            "replace": CONFUSION_ASSESSMENT_METHOD_SCORE,
        },
        # Confusion Assessment Method score
        {"code": CONFUSION_ASSESSMENT_METHOD_SCORE.concept_code, "vocabulary": DigiPOD},
        # Delirium Rating Scale score
        {"code": DELIRIUM_RATING_SCALE_SCORE.concept_code, "vocabulary": DigiPOD},
        # Delirium Observation Scale score
        {"code": DELIRIUM_OBSERVATION_SCALE_SCORE.concept_code, "vocabulary": DigiPOD},
        # 3-minute Diagnostic Interview for CAM-defined Delirium score
        {
            "code": THREE_MINUTE_DIAGNOSTIC_INTERVIEW_FOR_CAM_DEFINED_DELIRIUM_SCORE.concept_code,
            "vocabulary": DigiPOD,
        },
        # Confusion Assessment Method for the Intensive Care Unit score
        {
            "code": CONFUSION_ASSESSMENT_METHOD_FOR_THE_INTENSIVE_CARE_UNIT_SCORE.concept_code,
            "vocabulary": DigiPOD,
        },
        # Delirium Detection Score score
        {"code": DELIRIUM_DETECTION_SCORE_SCORE.concept_code, "vocabulary": DigiPOD},
        # 4 A's Test for delirium and cognitive impairment score (observable entity)
        {"code": "1239211000000103", "vocabulary": SNOMEDCT},
        # Presence of optimizable preoperative risk factor
        {
            "code": OPTIMIZABLE_PREOPERATIVE_RISK_FACTOR.concept_code,
            "vocabulary": DigiPOD,
        },
        # Charlson Comorbidity Index score
        {
            "code": RESULT_OF_CHARLSON_COMORBIDITY_INDEX.concept_code,
            "vocabulary": DigiPOD,
        },
        # $sct-uk#711061000000109 "Addenbrooke's cognitive examination revised - score (observable entity)"
        {"code": ACE_R.concept_code, "vocabulary": SNOMEDCT},
        # $sct#1255891005 "Montreal Cognitive Assessment version 8.1 score (observable entity)"
        {"code": MOCA.concept_code, "vocabulary": SNOMEDCT},
        # $loinc#72172-0 "Total score [MoCA]"
        {"code": MOCA_LOINC.concept_code, "vocabulary": LOINC},
        # $sct#302132005 "American Society of Anesthesiologists physical status class (observable entity)"
        {"code": ASA.concept_code, "vocabulary": SNOMEDCT},
        # $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
        {"code": MINICOG.concept_code, "vocabulary": SNOMEDCT},
        # $sct#447316007 "Mini-mental state examination score (observable entity)"
        {"code": MMSE.concept_code, "vocabulary": SNOMEDCT},
        {"code": FACES_ANXIETY_SCALE_SCORE.concept_code, "vocabulary": DigiPOD},
    ]

    @classmethod
    def resolve_concept(cls, characteristic: EvidenceVariableCharacteristic) -> Concept:
        """
        Resolves the corresponding OMOP Concept for the given FHIR characteristic.

        :param characteristic: An EvidenceVariableCharacteristic containing a coded concept definition.
        :return: The matching OMOP Concept, either from predefined mappings or dynamically retrieved.
        :raises ValueError: If no matching concept is found.
        """
        cc = get_coding(characteristic.definitionByTypeAndValue.type)
        for concept_entry in cls._concepts:
            if (
                concept_entry["vocabulary"].is_system(cc.system)
                and cc.code == concept_entry["code"]
            ):
                if "replace" in concept_entry:
                    return concept_entry["replace"]

                try:
                    # try to find a standard code first
                    concept = parse_code(
                        characteristic.definitionByTypeAndValue.type, standard=True
                    )
                except ValueError:
                    # fallback to non-standard
                    concept = parse_code(
                        characteristic.definitionByTypeAndValue.type, standard=False
                    )
                return concept

        raise ValueError(f"Concept {cc.system}#{cc.code} not found")

    @classmethod
    def from_fhir(
        cls, characteristic: EvidenceVariableCharacteristic
    ) -> AbstractCharacteristic:
        """Creates a new Characteristic instance from a FHIR EvidenceVariable.characteristic."""
        assert cls.valid(characteristic), "Invalid characteristic definition"

        type_omop_concept = cls.resolve_concept(characteristic)
        value = parse_value(
            value_parent=characteristic.definitionByTypeAndValue, value_prefix="value"
        )

        c: AbstractCharacteristic = cls(exclude=characteristic.exclude)
        c.type = type_omop_concept
        c.value = value

        return c

    @classmethod
    def valid(
        cls,
        char_definition: EvidenceVariableCharacteristic,
    ) -> bool:
        """Checks if the given FHIR definition is a valid action in the context of CPG-on-EBM-on-FHIR."""
        cc = get_coding(char_definition.definitionByTypeAndValue.type)

        for concept in cls._concepts:
            if (
                concept["vocabulary"].is_system(cc.system)
                and cc.code == concept["code"]
            ):
                return True
        return False

    def to_positive_expression(self) -> logic.Symbol:
        """Converts this characteristic to a Criterion."""

        cls: Type[ConceptCriterion]

        match self.type.domain_id:
            case "Procedure":
                cls = ProcedureOccurrence
            case "Measurement":
                cls = Measurement
            case "Observation":
                cls = Observation
            case _:
                raise ValueError(
                    f"Concept domain {self.type.domain_id} is not supported for AssessmentAction"
                )

        criterion = cls(concept=self.type, value=self.value)

        return criterion
