from execution_engine.converter.relative_time.abstract import RelativeTime
from execution_engine.omop.vocabulary import standard_vocabulary
from execution_engine.util import logic
from execution_engine.util.value import ValueNumber, ValueScalar

from digipod.terminology.vocabulary import FACES_ANXIETY_SCALE_SCORE, DigiPOD


class OnDayOfFacesAnxietyScaleAssessment(RelativeTime):
    """
    On the day of the Faces Anxiety Scale score
    """

    _event_vocabulary = DigiPOD
    _event_code = FACES_ANXIETY_SCALE_SCORE.concept_code

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """

        from digipod.criterion.observations import (
            BeforeDailyFacesAnxietyScaleAssessment,
            OnFacesAnxietyScaleAssessmentDay,
        )

        if self._value == ValueNumber(
            value=0, unit=standard_vocabulary.get_standard_unit_concept("d")
        ):
            return OnFacesAnxietyScaleAssessmentDay()
        elif self._value == ValueScalar(value_max=0):
            return BeforeDailyFacesAnxietyScaleAssessment()
        else:
            raise NotImplementedError("Not Implemented")
