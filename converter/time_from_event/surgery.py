from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.omop.vocabulary import LOINC, SNOMEDCT
from execution_engine.util import logic
from execution_engine.util.value.value import ValueScalar

from digipod.terminology import vocabulary

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

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
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

            return PreOperativePatientsBeforeDayOfSurgery()

        raise NotImplementedError(
            "Currently, only preoperative patients are implemented"
        )


class PreOperative(TimeFromEvent):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = SNOMEDCT
    _event_code = "262068006"  # Surgical operation date

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        if self._value is not None:
            raise NotImplementedError(
                "Only pre-surgical without a condition implemented"
            )

        from digipod.criterion.preop_patients import PreOperativePatientsBeforeSurgery

        return PreOperativePatientsBeforeSurgery()


class IntraPostOperative(TimeFromEvent):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = LOINC
    _event_code = "80992-1"  # Date and time of surgery

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        if self._value is not None and self._value != ValueScalar(value_min=0):
            raise NotImplementedError(
                "Only pre-surgical without a condition implemented"
            )

        from digipod.criterion.intraop_patients import IntraOperativePatients

        return IntraOperativePatients()


class PostOperative(TimeFromEvent):
    """
    This class represents the criterion of the time after a surgery
    """

    _event_vocabulary = SNOMEDCT
    _event_code = "262061000"  # Postoperative period

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        if self._value is not None and self._value != ValueScalar(value_min=0):
            raise NotImplementedError(
                "Only post-surgical without a condition implemented"
            )

        from digipod.criterion.postop_patients import PostOperativePatients

        return PostOperativePatients()


class PreOrIntraOperative(TimeFromEvent):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = SNOMEDCT
    _event_code = "442137000"  # Completion time of procedure (observable entity)

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """
        assert self._value is not None
        if (
            self._value.value_min == -1008
            and self._value.value_max == 0
            and self._value.unit.concept_code == "h"
        ):

            from digipod.criterion.preop_patients import (
                PreOperativePatientsBeforeEndOfSurgery,
            )

            return PreOperativePatientsBeforeEndOfSurgery()

        raise NotImplementedError(
            "Currently, only pre/intraoperative patients before end of surgery are implemented"
        )


# Todo: this should be the same as above (actually the digipod code shouldn't exist, because it's the same)
class PreOrIntraOperativeDigipod(TimeFromEvent):
    """
    This class represents the criterion of the time before the surgery
    """

    _event_vocabulary = vocabulary.DigiPOD
    _event_code = str(
        vocabulary.COMPLETION_TIME_OF_SURGICAL_PROCEDURE.concept_code
    )  # Completion time of surgical procedure

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """
        assert self._value is not None
        if (
            self._value.value_min == -1008
            and self._value.value_max == 0
            and self._value.unit.concept_code == "h"
        ):

            from digipod.criterion.preop_patients import (
                PreOperativePatientsBeforeEndOfSurgery,
            )

            return PreOperativePatientsBeforeEndOfSurgery()

        raise NotImplementedError(
            "Currently, only pre/intraoperative patients before end of surgery are implemented"
        )
