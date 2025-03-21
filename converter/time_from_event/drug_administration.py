from execution_engine.converter.time_from_event.abstract import TimeFromEvent
from execution_engine.util import logic

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

    def to_interval_criterion(self) -> logic.BaseExpr:
        """
        Returns the criterion that returns the intervals during the enclosed criterion/combination is evaluated.
        """
        return PatientsBeforeFirstDexAdministration()
