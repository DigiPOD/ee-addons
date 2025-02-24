from execution_engine.converter.characteristic.abstract import AbstractCharacteristic
from execution_engine.converter.criterion import Criterion, parse_code, parse_value
from execution_engine.fhir.util import get_coding
from execution_engine.omop.vocabulary import SNOMEDCT
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic


class AgeConverter(AbstractCharacteristic):
    """
    Converts Age criteria
    """

    _concept_code = "424144002"  # Ventilator care management (procedure)
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

    def to_positive_criterion(self) -> Criterion:
        """Converts this characteristic to a Criterion."""
        from digipod.criterion.patients import AgeLimitPatient

        return AgeLimitPatient(min_age_years=self.value.value_min)
