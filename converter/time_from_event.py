from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.temporal import (
    TemporalIndicatorCombination,
)
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


class SurgicalOperationDate(TimeFromEvent):
    """
    This class represents the criterion of the time from the surgical operation date
    """

    _event_vocabulary = LOINC
    _event_code = "67782-3"  # Surgical operation date

    def to_temporal_combination(
        self, mode: str
    ) -> TemporalIndicatorCombination | Criterion:
        """
        Returns a temporal combination of the criterion based on the mode

        Args:
            mode: The mode of the criterion (population or filter)

        Returns:
            TemporalIndicatorCombination: The temporal combination of the criterion
        """

        assert self._value is not None
        if (
            self._value.value_min == -1008
            and self._value.value_max == -2
            and self._value.unit.concept_code == "h"
        ):

            if mode == "population":
                from digipod.criterion.preop_patients import (
                    PreOperativePatientsBeforeDayOfSurgery,
                )

                return PreOperativePatientsBeforeDayOfSurgery()

        raise NotImplementedError(
            "Currently, only preoperative patients are implemented"
        )
