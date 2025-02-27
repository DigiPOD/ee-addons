import logging
from typing import Callable

from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.combination import CriterionCombination
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    PersonalWindowTemporalIndicatorCombination,
    TemporalIndicatorCombination,
)
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence


def _wrap_criteria_with_factory(
    combo: Criterion | CriterionCombination,
    factory: Callable[[Criterion | CriterionCombination], TemporalIndicatorCombination],
) -> CriterionCombination:
    """
    Recursively wraps all Criterion instances within a combination using the specified factory.

    :param combo: A single Criterion or a CriterionCombination to be processed.
    :param factory: A callable that takes a Criterion or CriterionCombination and returns a TemporalIndicatorCombination.
    :return: A new CriterionCombination where all Criterion instances have been wrapped using the factory.
    :raises ValueError: If an unexpected element type is encountered.
    """

    from digipod.concepts import OMOP_SURGICAL_PROCEDURE

    new_combo: CriterionCombination

    if isinstance(combo, Criterion):
        new_combo = factory(combo)
    elif isinstance(combo, CriterionCombination):

        # Create a new combination of the same type with the same operator
        new_combo = combo.__class__(operator=combo.operator)

        # Loop through all elements
        for element in combo:
            if isinstance(element, LogicalCriterionCombination):
                # Recursively wrap nested combinations
                new_combo.add(_wrap_criteria_with_factory(element, factory))
            elif isinstance(element, Criterion):
                # Wrap individual criteria with the factory

                if (
                    isinstance(element, ProcedureOccurrence)
                    and element.concept.concept_id == OMOP_SURGICAL_PROCEDURE
                    and element.concept.vocabulary_id == "SNOMED"
                ):
                    logging.warning(
                        "Removing Surgical Procedure Criterion in TimeFromEvent-SurgicalOperationDate"
                    )
                    continue

                new_combo.add(factory(element))
            else:
                raise ValueError(f"Unexpected element type: {type(element)}")
    else:
        raise ValueError(f"Unexpected element type: {type(combo)}")

    return new_combo


def wrap_criteria_with_temporal_indicator(
    combo: Criterion | CriterionCombination,
    interval_criterion: Criterion | CriterionCombination,
) -> CriterionCombination:
    """
    Wraps all Criterion instances in a combination with a PersonalWindowTemporalIndicatorCombination.

    :param combo: A single Criterion or a CriterionCombination to be wrapped.
    :param interval_criterion: A Criterion or CriterionCombination that defines the temporal interval.
    :return: A new CriterionCombination where all Criterion instances are wrapped with a PersonalWindowTemporalIndicatorCombination.
    """
    temporal_combo_factory = (
        lambda criterion: PersonalWindowTemporalIndicatorCombination.Presence(
            criterion=criterion, interval_criterion=interval_criterion
        )
    )

    new_combo = _wrap_criteria_with_factory(combo, temporal_combo_factory)

    return new_combo
