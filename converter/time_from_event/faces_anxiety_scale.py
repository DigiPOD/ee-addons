from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.util import logic
from execution_engine.util.value import ValueScalar

from digipod.terminology.vocabulary import FACES_ANXIETY_SCALE_SCORE, DigiPOD


class BeforeDailyFacesAnxietyScaleAssessment(TimeFromEvent):
    """
    Before the assessment and documentation of the Faces Anxiety Scale score of the day
    """

    _event_vocabulary = DigiPOD
    _event_code = FACES_ANXIETY_SCALE_SCORE.concept_code

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """
        if self._value != ValueScalar.parse("<=0"):
            raise NotImplementedError("Not Implemented")

        from digipod.criterion.observations import (
            BeforeDailyFacesAnxietyScaleAssessment,
        )

        return BeforeDailyFacesAnxietyScaleAssessment()
