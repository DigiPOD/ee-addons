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
from execution_engine.omop.vocabulary import SNOMEDCT, AbstractVocabulary
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic

from digipod.terminology.vocabulary import (
    CAM,
    CAM_ICU,
    DDS,
    DOS,
    DRS,
    ICDSC,
    DigiPOD,
    NuDESC,
    ThreeDCAM,
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
        # "Nursing Delirium Screening Scale (NU-DESC) score"
        {"code": NuDESC.concept_code, "vocabulary": DigiPOD},
        # "Intensive Care Delirium Screening Checklist score (observable entity)"
        {"code": "1351995008", "vocabulary": SNOMEDCT, "replace": ICDSC},
        # "Confusion Assessment Method score (observable entity)"
        {"code": "1351493007", "vocabulary": SNOMEDCT, "replace": CAM},
        #  "Delirium Rating Scale score"
        {"code": DRS.concept_code, "vocabulary": DigiPOD},
        # "Delirium Observation Scale score"
        {"code": DOS.concept_code, "vocabulary": DigiPOD},
        # "3-minute Diagnostic Interview for CAM-defined Delirium score"
        {"code": ThreeDCAM.concept_code, "vocabulary": DigiPOD},
        # "Confusion Assessment Method for the Intensive Care Unit score"
        {"code": CAM_ICU.concept_code, "vocabulary": DigiPOD},
        # "Delirium Detection Score score"
        {"code": DDS.concept_code, "vocabulary": DigiPOD},
        # "4 A's Test for delirium and cognitive impairment score (observable entity)"
        {"code": "1239211000000103", "vocabulary": SNOMEDCT},
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

    def to_positive_criterion(self) -> ConceptCriterion:
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
