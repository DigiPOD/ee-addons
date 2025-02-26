import logging
from typing import Callable

from execution_engine.converter.time_from_event.abstract import TimeFromEvent
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
from execution_engine.omop.vocabulary import LOINC

#  $loinc#67782-3 "Surgical operation date"
#  $sct#442137000 "Completion time of procedure (observable entity)"
# $cs-digipod#034 "Completion time of surgical procedure" //$sct#442137000 "Completion time of procedure (observable entity)"
# $loinc#80992-1 "Date and time of surgery"
# $cs-digipod#029 "Before dexmedetomidine administration"
# $cs-digipod#030 "After dexmedetomidine administration"
# $sct#277671009 "Intraoperative (qualifier value)"
# $sct#262068006 "Preoperative (qualifier value)"
# $sct#262061000 "Postoperative period (qualifier value)"


def _wrap_criteria_with_factory(
    combo: Criterion | CriterionCombination,
    factory: Callable[[Criterion | CriterionCombination], TemporalIndicatorCombination],
) -> CriterionCombination:
    """
    Recursively wraps all Criterion instances within a combination using the factory.
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


class SurgicalOperationDate(TimeFromEvent):
    """
    This class represents the criterion of the time from the surgical operation date
    """

    _event_vocabulary = LOINC
    _event_code = "67782-3"  # Surgical operation date

    def to_temporal_combination(
        self, combo: Criterion | CriterionCombination
    ) -> CriterionCombination:
        """
        Returns a temporal combination of the criterion based on the mode

        Returns:
            TemporalIndicatorCombination: The temporal combination of the criterion
        """

        assert self._value is not None
        if (
            self._value.value_min == -1008
            and self._value.value_max == -2
            and self._value.unit.concept_code == "h"
        ):

            from digipod.criterion.preop_patients import (
                PreOperativePatientsBeforeDayOfSurgery,
            )

            interval_criterion = PreOperativePatientsBeforeDayOfSurgery()

            temporal_combo_factory = (
                lambda criterion: PersonalWindowTemporalIndicatorCombination.Presence(
                    criterion=criterion, interval_criterion=interval_criterion
                )
            )

            new_combo = _wrap_criteria_with_factory(combo, temporal_combo_factory)

            return new_combo

        raise NotImplementedError(
            "Currently, only preoperative patients are implemented"
        )
