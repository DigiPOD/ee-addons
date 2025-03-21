from execution_engine.converter.relative_time.abstract import RelativeTime
from execution_engine.omop.vocabulary import LOINC
from execution_engine.util import logic
from execution_engine.util.value.value import ValueScalar


class BeforeDischarge(RelativeTime):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = LOINC
    _event_code = "75523-1"  # Discharge time

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        if self._value is not None and self._value != ValueScalar(value_max=0):
            raise NotImplementedError(
                "Only pre-discharge without a condition implemented"
            )

        from execution_engine.omop.criterion.visit_occurrence import (
            PatientsActiveDuringPeriod,
        )

        return PatientsActiveDuringPeriod()
