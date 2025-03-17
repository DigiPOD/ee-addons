from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.util import logic

from digipod.converter.time_from_event.util import wrap_criteria_with_temporal_indicator
from digipod.criterion import PatientsBeforeFirstDexAdministration
from digipod.terminology import vocabulary
from digipod.terminology.vocabulary import DigiPOD


class BeforeDexmedetomidineAdministration(TimeFromEvent):
    """
    This class represents the criterion of the time from a drug administration
    """

    # _event_vocabulary = SNOMEDCT
    # _event_code = "432102000"  # "Administration of substance (procedure)"
    _event_vocabulary = DigiPOD
    _event_code = vocabulary.BEFORE_DEXMEDETOMIDINE_ADMINISTRATION.concept_code

    def to_temporal_combination(self, expr: logic.BaseExpr) -> logic.Expr:
        """
        Returns a temporal combination of the criterion based on the mode

        Returns:
            TemporalIndicatorCombination: The temporal combination of the criterion
        """

        return wrap_criteria_with_temporal_indicator(
            expr, PatientsBeforeFirstDexAdministration()
        )
