import logging
from typing import Self

from execution_engine.converter.action.abstract import AbstractAction
from execution_engine.converter.action.assessment import AssessmentAction
from execution_engine.converter.action.procedure import ProcedureAction
from execution_engine.converter.criterion import parse_code
from execution_engine.fhir.recommendation import RecommendationPlan
from execution_engine.fhir.util import get_coding
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.vocabulary import SNOMEDCT

from digipod.converter.characteristic.observation import ConceptEntry
from digipod.criterion.noop import Noop
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


class AssessmentActionConverter(AssessmentAction):
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
        # "Delirium Rating Scale score"
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
    def resolve_concept(cls, action_def: RecommendationPlan.Action) -> Concept:
        """
        Resolves the corresponding OMOP Concept for the given FHIR characteristic.

        :param action_def: An RecommendationPlan.Action containing a coded concept definition.
        :return: The matching OMOP Concept, either from predefined mappings or dynamically retrieved.
        :raises ValueError: If no matching concept is found.
        """

        assert (
            action_def.activity_definition_fhir is not None
        ), "ActivityDefinition is required"

        cc = get_coding(action_def.activity_definition_fhir.code)

        for concept_entry in cls._concepts:
            if (
                concept_entry["vocabulary"].is_system(cc.system)
                and cc.code == concept_entry["code"]
            ):
                if "replace" in concept_entry:
                    return concept_entry["replace"]

                assert (
                    action_def.activity_definition_fhir is not None
                ), "ActivityDefinition is required"

                try:
                    # try to find a standard code first
                    concept = parse_code(
                        action_def.activity_definition_fhir.code, standard=True
                    )
                except ValueError:
                    # fallback to non-standard
                    concept = parse_code(
                        action_def.activity_definition_fhir.code, standard=False
                    )
                return concept

        raise ValueError(f"Concept {cc.system}#{cc.code} not found")

    @classmethod
    def from_fhir(cls, action_def: RecommendationPlan.Action) -> "AbstractAction":
        """Creates a new action from a FHIR PlanDefinition."""
        assert cls.valid(action_def), "Invalid characteristic definition"

        assert (
            action_def.activity_definition_fhir is not None
        ), "ActivityDefinition is required"

        code = cls.resolve_concept(action_def)

        if action_def.activity_definition_fhir.timingTiming is not None:
            timing = cls.process_timing(
                action_def.activity_definition_fhir.timingTiming
            )
        else:
            timing = None

        exclude = action_def.activity_definition_fhir.doNotPerform

        return cls(exclude=exclude, code=code, timing=timing)

    @classmethod
    def valid(
        cls,
        action_def: RecommendationPlan.Action,
    ) -> bool:
        """Checks if the given FHIR definition is a valid action in the context of CPG-on-EBM-on-FHIR."""

        if not super().valid(action_def):
            return False

        assert (
            action_def.activity_definition_fhir is not None
        ), "ActivityDefinition is required"

        cc = get_coding(action_def.activity_definition_fhir.code)

        for concept in cls._concepts:
            if (
                concept["vocabulary"].is_system(cc.system)
                and cc.code == concept["code"]
            ):
                return True
        return False
