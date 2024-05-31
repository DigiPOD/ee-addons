import datetime
from typing import Any, Dict, Self

from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.abstract import (
    Criterion,
    column_interval_type,
    observation_end_datetime,
    observation_start_datetime,
)
from execution_engine.omop.db.omop.tables import Person, ProcedureOccurrence
from execution_engine.util.interval import IntervalType
from sqlalchemy import Select, select


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


class PatientsInTimeFrame(Criterion):
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
        return self.__class__.__name__

    def dict(self) -> dict:
        """
        Get a dictionary representation of the object.
        """
        return {
            "exclude": self._exclude,
            "category": self.category.value,
            "class": self.__class__.__name__,
        }
