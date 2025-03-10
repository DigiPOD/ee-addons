from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.combination import CriterionCombination

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

    def to_temporal_combination(
        self, combo: Criterion | CriterionCombination
    ) -> CriterionCombination:
        """
        Returns a temporal combination of the criterion based on the mode

        Returns:
            TemporalIndicatorCombination: The temporal combination of the criterion
        """

        return wrap_criteria_with_temporal_indicator(
            combo, PatientsBeforeFirstDexAdministration()
        )
