from execution_engine.converter.relative_time.abstract import RelativeTime
from execution_engine.omop.vocabulary import LOINC
from execution_engine.util import logic
from execution_engine.util.value.value import ValueScalar

from digipod.terminology.vocabulary import DigiPOD


class PostOperative(RelativeTime):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = DigiPOD
    _event_code = "034"  # Completion time of surgical procedure"

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        if self._value is not None and self._value != ValueScalar(value_min=0):
            raise NotImplementedError(
                "Only post-surgical without a condition implemented"
            )

        from digipod.criterion import PostOperativePatients

        return PostOperativePatients()


class IntraOrPostOperative(RelativeTime):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = LOINC
    _event_code = "80992-1"  # Date and time of surgery"

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        if self._value is not None and self._value != ValueScalar(value_min=0):
            raise NotImplementedError(
                "Only post-surgical without a condition implemented"
            )

        from digipod.criterion import IntraOrPostOperativePatients

        return IntraOrPostOperativePatients()
