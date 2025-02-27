import logging
from typing import Self

from execution_engine.converter.action.abstract import AbstractAction
from execution_engine.converter.action.procedure import ProcedureAction
from execution_engine.converter.criterion import parse_code
from execution_engine.fhir.recommendation import RecommendationPlan
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.vocabulary import SNOMEDCT

from digipod.criterion.noop import Noop


class NoopAction(AbstractAction):
    """
    A no-operation (noop) action that does not generate any criteria.

    This action is used when a recommendation does not require a specific operational criterion.
    """

    @classmethod
    def from_fhir(cls, action_def: RecommendationPlan.Action) -> Self:
        """Creates a new action from a FHIR PlanDefinition."""
        assert (
            action_def.activity_definition_fhir is not None
        ), "ActivityDefinition is required"

        exclude = action_def.activity_definition_fhir.doNotPerform

        return cls(exclude=exclude)

    def _to_criterion(self) -> Criterion | LogicalCriterionCombination | None:
        return Noop()


class OtherActionConverter(ProcedureAction):
    """
    Converts "Other" Actions (from the "other" slice in FHIR Actions).
    """

    _concept_code = "74964007"  # "Other (qualifier value)"
    _concept_vocabulary = SNOMEDCT

    @classmethod
    def from_fhir(cls, action_def: RecommendationPlan.Action) -> AbstractAction:
        """Creates a new action from a FHIR PlanDefinition."""
        assert (
            action_def.activity_definition_fhir is not None
        ), "ActivityDefinition is required"
        assert (
            action_def.activity_definition_fhir.code is not None
        ), "Code is required for Other Action"

        if action_def.activity_definition_fhir.code.coding is None:
            logging.warning("No coding in action - returning Noop Action")
            return NoopAction.from_fhir(action_def)

        code = parse_code(action_def.activity_definition_fhir.code)

        if action_def.activity_definition_fhir.timingTiming is not None:
            timing = cls.process_timing(
                action_def.activity_definition_fhir.timingTiming
            )
        else:
            timing = None

        exclude = action_def.activity_definition_fhir.doNotPerform

        return cls(exclude=exclude, code=code, timing=timing)
