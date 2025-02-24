from typing import Self, Type

from execution_engine.constants import CohortCategory
from execution_engine.converter.action.abstract import AbstractAction
from execution_engine.converter.characteristic.abstract import AbstractCharacteristic
from execution_engine.converter.characteristic.value import AbstractValueCharacteristic
from execution_engine.converter.criterion import parse_code, parse_value
from execution_engine.fhir.recommendation import RecommendationPlan
from execution_engine.fhir.util import get_coding
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.concept import ConceptCriterion
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.vocabulary import SNOMEDCT
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept
from fhir.resources.evidencevariable import EvidenceVariableCharacteristic


class OtherActionConverter(AbstractAction):
    """
    Converts "Other" Actions (from the "other" slice in FHIR Actions).
    """

    _concept_code = "74964007"  # "Other (qualifier value)"
    _concept_vocabulary = SNOMEDCT

    def __init__(
        self,
        exclude: bool,
        code: Concept,
        timing: Timing | None = None,
    ) -> None:
        """
        Initialize the assessment action.
        """
        super().__init__(exclude=exclude)
        self._code = code
        self._timing = timing

    @classmethod
    def from_fhir(cls, action_def: RecommendationPlan.Action) -> Self:
        """Creates a new action from a FHIR PlanDefinition."""
        assert (
            action_def.activity_definition_fhir is not None
        ), "ActivityDefinition is required"
        assert (
            action_def.activity_definition_fhir.code is not None
        ), "Code is required for Other Action"

        code = parse_code(action_def.activity_definition_fhir.code)

        if action_def.activity_definition_fhir.timingTiming is not None:
            timing = cls.process_timing(
                action_def.activity_definition_fhir.timingTiming
            )
        else:
            timing = None

        exclude = action_def.activity_definition_fhir.doNotPerform

        return cls(exclude=exclude, code=code, timing=timing)

    def _to_criterion(self) -> Criterion | LogicalCriterionCombination | None:
        """Converts this characteristic to a Criterion."""

        cls: Type[ConceptCriterion]

        match self._code.domain_id:
            case "Procedure":
                cls = ProcedureOccurrence
            case "Measurement":
                cls = Measurement
            case "Observation":
                cls = Observation
            case _:
                raise ValueError(
                    f"Concept domain {self._code.domain_id} is not supported for AssessmentAction"
                )

        criterion = cls(
            category=CohortCategory.INTERVENTION,
            concept=self._code,
            timing=self._timing,
        )

        # we need to explicitly set the VALUE_REQUIRED flag to false after creation of the object,
        # otherwise creating the query will raise an error as Observation and Measurement normally expect
        # a value.
        criterion._OMOP_VALUE_REQUIRED = False

        return criterion

    # @classmethod
    # def valid(
    #     cls,
    #     action_def: RecommendationPlan.Action,
    # ) -> bool:
    #     """Checks if the given FHIR definition is a valid action in the context of CPG-on-EBM-on-FHIR."""
    #     cc = get_coding(action_def.activity_definition_fhir.code)
    #     return (
    #         cls._concept_vocabulary.is_system(cc.system)
    #         and cc.code == cls._concept_code
    #     )


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

        cls: Type[ConceptCriterion]

        assert isinstance(
            self.value, ValueConcept
        ), "Value must be instance of ValueConcept"

        concept = self.value.value

        match concept.domain_id:
            case "Procedure":
                cls = ProcedureOccurrence
            case "Measurement":
                cls = Measurement
            case "Observation":
                cls = Observation
            case _:
                raise ValueError(
                    f"Concept domain {concept.domain_id} is not supported for AssessmentAction"
                )

        criterion = cls(
            category=CohortCategory.POPULATION,
            concept=concept,
            # timing=self._timing, # not used currently (or ever?)
        )

        # we need to explicitly set the VALUE_REQUIRED flag to false after creation of the object,
        # otherwise creating the query will raise an error as Observation and Measurement normally expect
        # a value.
        criterion._OMOP_VALUE_REQUIRED = False

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
