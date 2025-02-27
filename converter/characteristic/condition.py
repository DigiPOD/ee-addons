from typing import Type

from execution_engine.converter.characteristic.codeable_concept import (
    AbstractCodeableConceptCharacteristic,
)
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.vocabulary import SNOMEDCT

SCT_CLINICAL_FINDING_PRESENT = "373573001"  # Clinical finding present (situation)


class DigiPODConditionCharacteristic(AbstractCodeableConceptCharacteristic):
    """A condition characteristic in the context of CPG-on-EBM-on-FHIR."""

    _concept_code = SCT_CLINICAL_FINDING_PRESENT
    _concept_vocabulary = SNOMEDCT
    _criterion_class = ConditionOccurrence
    _concept_value_static = False

    @classmethod
    def get_class_from_concept(
        cls, concept: Concept
    ) -> Type["AbstractCodeableConceptCharacteristic"]:
        """Gets the class that matches the given concept."""

        return cls
