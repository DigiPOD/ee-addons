from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.combination import CriterionCombination
from execution_engine.omop.vocabulary import SNOMEDCT

from digipod.converter.time_from_event.util import wrap_criteria_with_temporal_indicator


class DrugAdministration(TimeFromEvent):
    """
    This class represents the criterion of the time from a drug administration
    """

    _event_vocabulary = SNOMEDCT
    _event_code = "432102000"  # "Administration of substance (procedure)"

    def to_temporal_combination(
        self, combo: Criterion | CriterionCombination
    ) -> CriterionCombination:
        """
        Returns a temporal combination of the criterion based on the mode

        Returns:
            TemporalIndicatorCombination: The temporal combination of the criterion
        """

        assert self._value is not None, "Value must be supplied"
        if (
            self._value.value_min == -1008
            and self._value.value_max == -2
            and self._value.unit.concept_code == "h"
        ):

            from digipod.criterion.preop_patients import (
                PreOperativePatientsBeforeDayOfSurgery,
            )

            return wrap_criteria_with_temporal_indicator(
                combo, PreOperativePatientsBeforeDayOfSurgery()
            )

        raise NotImplementedError(
            "Currently, only preoperative patients are implemented"
        )
