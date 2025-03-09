from execution_engine.converter.characteristic.abstract import AbstractCharacteristic
from execution_engine.converter.characteristic.value import AbstractValueCharacteristic
from execution_engine.converter.criterion import parse_code, parse_value
from execution_engine.fhir.util import get_coding
from execution_engine.omop.criterion.concept import ConceptCriterion
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.vocabulary import SNOMEDCT
from execution_engine.util.value import ValueConcept
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic


class AssessmentCharacteristicConverter(AbstractValueCharacteristic):
    """
    Converts Evaluation Procedure Actions
    """

    _concept_code = "386053000"  # Evaluation procedure (procedure)
    _concept_vocabulary = SNOMEDCT

    @classmethod
    def from_fhir(
        cls, characteristic: EvidenceVariableCharacteristic
    ) -> AbstractCharacteristic:
        """Creates a new Characteristic instance from a FHIR EvidenceVariable.characteristic."""
        assert cls.valid(characteristic), "Invalid characteristic definition"

        type_omop_concept = parse_code(characteristic.definitionByTypeAndValue.type)
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
        return (
            cls._concept_vocabulary.is_system(cc.system)
            and cc.code == cls._concept_code
        )

    def to_positive_criterion(self) -> ConceptCriterion:
        """Converts this characteristic to a Criterion."""

        criterion: ConceptCriterion

        assert isinstance(
            self.value, ValueConcept
        ), "Value must be instance of ValueConcept"

        concept = self.value.value

        match concept.domain_id:
            case "Procedure":
                criterion = ProcedureOccurrence(
                    concept=concept,
                    # timing=self._timing, # not used currently (or ever?)
                )
            case "Measurement":
                # we need to explicitly set the VALUE_REQUIRED flag to false, otherwise creating the query will raise an error
                # as Observation and Measurement normally expect a value.
                criterion = Measurement(
                    concept=concept,
                    override_value_required=False,
                    # timing=self._timing, # not used currently (or ever?)
                )
            case "Observation":
                # we need to explicitly set the VALUE_REQUIRED flag to false, otherwise creating the query will raise an error
                # as Observation and Measurement normally expect a value.
                criterion = Observation(
                    concept=concept,
                    override_value_required=False,
                    # timing=self._timing, # not used currently (or ever?)
                )
            case _:
                raise ValueError(
                    f"Concept domain {concept.domain_id} is not supported for AssessmentAction"
                )

        return criterion


class ProcedureWithExplicitContextConverter(AssessmentCharacteristicConverter):
    """
    Converts Evaluation Procedure Actions
    """

    _concept_code = "129125009"  # "Procedure with explicit context (situation)"
    _concept_vocabulary = SNOMEDCT

    @classmethod
    def from_fhir(
        cls, characteristic: EvidenceVariableCharacteristic
    ) -> AbstractCharacteristic:
        """Creates a new Characteristic instance from a FHIR EvidenceVariable.characteristic."""
        assert cls.valid(characteristic), "Invalid characteristic definition"

        type_omop_concept = parse_code(characteristic.definitionByTypeAndValue.type)
        value = parse_value(
            value_parent=characteristic.definitionByTypeAndValue,
            value_prefix="value",
            standard=False,
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
        return (
            cls._concept_vocabulary.is_system(cc.system)
            and cc.code == cls._concept_code
        )
