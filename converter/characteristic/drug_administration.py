from execution_engine.converter.characteristic.abstract import AbstractCharacteristic
from execution_engine.converter.criterion import parse_code, parse_value
from execution_engine.fhir.util import get_coding
from execution_engine.omop.criterion.drug_exposure import DrugExposure
from execution_engine.omop.vocabulary import SNOMEDCT
from execution_engine.util import logic
from execution_engine.util.value import ValueConcept
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic


class DrugAdministrationCharacteristicConverter(AbstractCharacteristic):
    """
    Converts DrugAdministration characteristics
    """

    _concept_code = "18629005"  # Administration of drug or medicament (procedure)
    _concept_vocabulary = SNOMEDCT

    @classmethod
    def from_fhir(
        cls, characteristic: EvidenceVariableCharacteristic
    ) -> AbstractCharacteristic:
        """Creates a new Characteristic instance from a FHIR EvidenceVariable.characteristic."""
        assert cls.valid(characteristic), "Invalid characteristic definition"

        type_omop_concept = parse_code(characteristic.definitionByTypeAndValue.type)

        try:
            value = parse_value(
                value_parent=characteristic.definitionByTypeAndValue,
                value_prefix="value",
                standard=True,
            )
        except ValueError:
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

    def to_positive_expression(self) -> logic.Symbol:
        """Converts this characteristic to a Criterion."""

        assert isinstance(
            self.value, ValueConcept
        ), "Value must be instance of ValueConcept"

        concept = self.value.value

        assert concept.domain_id == "Drug", "Value must be from the DrugExposure domain"

        criterion = DrugExposure(
            ingredient_concept=concept,
            dose=None,
            route=None,
            # timing=self._timing, # not used currently (or ever?)
        )

        return criterion
