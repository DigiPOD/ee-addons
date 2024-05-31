import datetime
from typing import Any, Dict, Self

from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.abstract import (
    Criterion,
    column_interval_type,
    observation_end_datetime,
    observation_start_datetime,
)
from execution_engine.omop.criterion.combination import CriterionCombination
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import VisitOccurrence
from execution_engine.omop.db.omop.tables import Person, ProcedureOccurrence
from execution_engine.util.interval import IntervalType
from execution_engine.util.value import ValueNumber
from sqlalchemy import Interval, func, select
from sqlalchemy.sql import Select

from digipod import concepts


class AdultPatients(Criterion):
    """
    Select patients who are at least 18 years old.
    """

    _static = True

    def __init__(self) -> None:
        super().__init__(exclude=False, category=CohortCategory.POPULATION)
        self._table = Person.__table__.alias("p")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        """
        Create an object from a dictionary.
        """
        return cls(**data)

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return "AdultPatients"

    def dict(self) -> dict:
        """
        Get a dictionary representation of the object.
        """
        return {
            "exclude": self._exclude,
            "category": self.category.value,
            "class": self.__class__.__name__,
        }

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """
        # Current date minus 18 years to find the maximum birth date for 18-year-olds
        eighteen_years_ago = datetime.datetime.now() - datetime.timedelta(
            days=18 * 365.25
        )

        query = select(
            self._table.c.person_id,
            observation_start_datetime.label("interval_start"),
            observation_end_datetime.label("interval_end"),
            column_interval_type(IntervalType.POSITIVE),
        ).where(self._table.c.birth_datetime <= eighteen_years_ago)

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


class PreOperativePatientsBeforeDayOfSurgery(Criterion):
    """
    Select patients who are pre-surgical in the timeframe between 42 days before the surgery and the day of the surgery.
    """

    _static = True

    def __init__(self) -> None:
        super().__init__(exclude=False, category=CohortCategory.POPULATION)
        self._table = ProcedureOccurrence.__table__.alias("po")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        """
        Create an object from a dictionary.
        """
        return cls(**data)

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return "PreOperativeAdultBeforeDayOfSurgeryPatients"

    def dict(self) -> dict:
        """
        Get a dictionary representation of the object.
        """
        return {
            "exclude": self._exclude,
            "category": self.category.value,
            "class": self.__class__.__name__,
        }

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        # Define the concept ID for the surgical procedure
        surgical_procedure_concept_id = 4322976  # OMOP procedure

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (
                func.date_trunc("day", self._table.c.procedure_datetime)
                - func.cast(func.concat(42, "day"), Interval)
            ).label("interval_start"),
            (
                func.date_trunc("day", self._table.c.procedure_datetime)
                - func.cast(func.concat(1, "day"), Interval)
            ).label("interval_end"),
        ).where(self._table.c.procedure_concept_id == surgical_procedure_concept_id)

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


# todo: potentially we need to require VISIT_DETAIL here
class PreAdmissionPatients(VisitOccurrence):
    """
    Select patients who have a pre-admission visit ("vorstationär").
    """

    def __init__(self) -> None:
        super().__init__(
            exclude=False,
            category=CohortCategory.POPULATION,
            concept=concepts.OutpatientVisit,
        )


class InpatientPatients(VisitOccurrence):
    """
    Select patients who have an inpatient visit ("normalstationär").
    """

    def __init__(self) -> None:
        super().__init__(
            exclude=False,
            category=CohortCategory.POPULATION,
            concept=concepts.InpatientVisit,
        )


MMSEgte3 = PointInTimeCriterion(
    category=CohortCategory.POPULATION,
    concept=concepts.MMSE,
    value=ValueNumber(value_min=3, unit=concepts.unit_score),
)


class PreOperativePatientsBeforeEndOfSurgery(Criterion):
    """
    Select patients who are pre-operative in the timeframe between 42 days before the surgery and the end of the surgery.
    """

    _static = True

    def __init__(self) -> None:
        super().__init__(exclude=False, category=CohortCategory.POPULATION)
        self._table = ProcedureOccurrence.__table__.alias("po")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        """
        Create an object from a dictionary.
        """
        return cls(**data)

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return "PreOperativePatientsBeforeEndOfSugergery"

    def dict(self) -> dict:
        """
        Get a dictionary representation of the object.
        """
        return {
            "exclude": self._exclude,
            "category": self.category.value,
            "class": self.__class__.__name__,
        }

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        # Define the concept ID for the surgical procedure
        surgical_procedure_concept_id = 4322976  # OMOP procedure

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (
                func.date_trunc("day", self._table.c.procedure_datetime)
                - func.cast(func.concat(42, "day"), Interval)
            ).label("interval_start"),
            self._table.c.procedure_end_datetime.label("interval_end"),
        ).where(self._table.c.procedure_concept_id == surgical_procedure_concept_id)

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


"""
- >= 18 years
- 42 days until end of day before surgery
"""
preOperativeAdultBeforeDayOfSurgeryPatients = CriterionCombination.And(
    AdultPatients(),
    PreOperativePatientsBeforeDayOfSurgery(),
    category=CohortCategory.POPULATION,
)

"""
- >= 18 years
- 42 days until end of day before surgery
- MMSE >= 3
"""
preOperativeAdultBeforeDayOfSurgeryPatientsMMSEgte3 = CriterionCombination.And(
    AdultPatients(),
    PreOperativePatientsBeforeDayOfSurgery(),
    MMSEgte3,
    category=CohortCategory.POPULATION,
)


"""
- vorstationär OR normalstationär
"""
preAdmissionOrInpatientPatients = CriterionCombination.Or(
    PreAdmissionPatients(),
    InpatientPatients(),
    category=CohortCategory.POPULATION,
)

"""
- >= 18 years
- 42 days before day of surgery until end of surgery
- vorstationär OR normalstationär
"""
adultPatientsPreoperativelyGeneralOnSurgeryDayAndBefore = CriterionCombination.And(
    AdultPatients(),
    PreOperativePatientsBeforeEndOfSurgery(),
    preAdmissionOrInpatientPatients,
    category=CohortCategory.POPULATION,
)
