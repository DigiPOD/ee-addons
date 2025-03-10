import logging
from typing import Type

from execution_engine.converter.characteristic.abstract import AbstractCharacteristic
from execution_engine.converter.characteristic.codeable_concept import (
    AbstractCodeableConceptCharacteristic,
)
from execution_engine.fhir.util import get_coding
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.vocabulary import ICD10CM, SNOMEDCT, AbstractVocabulary
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic

SCT_CLINICAL_FINDING_PRESENT = "373573001"  # Clinical finding present (situation)


class DigiPODConditionCharacteristic(AbstractCodeableConceptCharacteristic):
    """A condition characteristic in the context of CPG-on-EBM-on-FHIR."""

    _concept_code = SCT_CLINICAL_FINDING_PRESENT
    _concept_vocabulary: Type[AbstractVocabulary] = SNOMEDCT
    _criterion_class = ConditionOccurrence
    _concept_value_static = False

    @classmethod
    def get_class_from_concept(
        cls, concept: Concept
    ) -> Type["AbstractCodeableConceptCharacteristic"]:
        """Gets the class that matches the given concept."""

        return cls


class DigiPODConditionICDCharacteristic(DigiPODConditionCharacteristic):
    """A condition coded using an ICD code."""

    _concept_vocabulary = ICD10CM

    @classmethod
    def valid(
        cls,
        char_definition: EvidenceVariableCharacteristic,
    ) -> bool:
        """
        In contrast to usual concepts, we here check for definitionCodeableConcept instead
        of definitionByTypeAndValue.
        """

        if not char_definition.definitionCodeableConcept:
            return False

        cc = get_coding(char_definition.definitionCodeableConcept)

        return cls._concept_vocabulary.is_system(cc.system)

    @classmethod
    def from_fhir(
        cls, characteristic: EvidenceVariableCharacteristic
    ) -> AbstractCharacteristic:
        """Creates a new Characteristic instance from a FHIR EvidenceVariable.characteristic."""
        assert cls.valid(characteristic), "Invalid characteristic definition"

        cc = get_coding(characteristic.definitionCodeableConcept)

        try:
            omop_concept = cls.get_standard_concept(cc)
        except ValueError:
            logging.warning(
                f"Concept {cc.code} not found in standard vocabulary {cc.system}. Using non-standard vocabulary."
            )
            omop_concept = cls.get_concept(cc, standard=False)

        class_ = cls.get_class_from_concept(omop_concept)

        c = class_(exclude=characteristic.exclude)
        c.value = omop_concept

        return c
