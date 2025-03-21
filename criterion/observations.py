from execution_engine.omop.criterion.abstract import (
    SQL_ONE_SECOND,
    Criterion,
    column_interval_type,
)
from execution_engine.omop.criterion.concept import ConceptCriterion
from execution_engine.omop.vocabulary import SNOMEDCT, standard_vocabulary
from execution_engine.util.interval import IntervalType
from sqlalchemy import Interval, func, select
from sqlalchemy.sql import Select

from digipod.terminology.custom_concepts import FACES_ANXIETY_SCALE_SCORE


class AfterDailyFacesAnxietyScaleAssessment(Criterion):
    """
    Select patients who are after the assessment and documentation of the Faces Anxiety Scale score of the day.
    """

    def description(self) -> str:
        """
        Get a string representation.
        """
        return "AfterDailyFacesAnxietyScaleAssessment"

    def __init__(self) -> None:
        super().__init__()
        self._set_omop_variables_from_domain(FACES_ANXIETY_SCALE_SCORE.domain_id)

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            self._table.c.measurement_datetime.label("interval_start"),
            (
                func.date_trunc("day", self._table.c.measurement_datetime)
                + func.cast(func.concat(1, "day"), Interval)
                - SQL_ONE_SECOND
            ).label("interval_end"),
        ).where(
            self._table.c.procedure_concept_id == FACES_ANXIETY_SCALE_SCORE.concept_id
        )

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


class BeforeDailyFacesAnxietyScaleAssessment(Criterion):
    """
    Select patients who are before the assessment and documentation of the Faces Anxiety Scale score of the day.
    """

    def description(self) -> str:
        """
        Get a string representation.
        """
        return "BeforeDailyFacesAnxietyScaleAssessment"

    def __init__(self) -> None:
        super().__init__()
        self._set_omop_variables_from_domain(FACES_ANXIETY_SCALE_SCORE.domain_id)
        self._value_required = False  # we don't care for any specific value

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            func.date_trunc("day", self._table.c.measurement_datetime).label(
                "interval_start"
            ),
            self._table.c.measurement_datetime.label("interval_end"),
        ).where(
            self._table.c.measurement_concept_id == FACES_ANXIETY_SCALE_SCORE.concept_id
        )

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


class OnFacesAnxietyScaleAssessmentDay(Criterion):
    """
    Select patients on the day of assessment and documentation of the Faces Anxiety Scale score.
    """

    def description(self) -> str:
        """
        Get a string representation.
        """
        return "OnFacesAnxietyScaleAssessmentDay"

    def __init__(self) -> None:
        super().__init__()
        self._set_omop_variables_from_domain(FACES_ANXIETY_SCALE_SCORE.domain_id)
        self._value_required = False  # we don't care for any specific value

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            func.date_trunc("day", self._table.c.measurement_datetime).label(
                "interval_start"
            ),
            (
                func.date_trunc("day", self._table.c.measurement_datetime)
                + func.cast(func.concat(1, "day"), Interval)
                - SQL_ONE_SECOND
            ).label("interval_end"),
        ).where(
            self._table.c.measurement_concept_id == FACES_ANXIETY_SCALE_SCORE.concept_id
        )

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


class Deglutition(ConceptCriterion):
    """
    Select patients on the day of Deglutition.
    """

    def description(self) -> str:
        """
        Get a string representation of this criterion.
        """
        return "Deglutition"

    def __init__(self) -> None:
        concept = standard_vocabulary.get_concept(
            system_uri=SNOMEDCT.system_uri, concept="54731003"
        )
        super().__init__(concept)
