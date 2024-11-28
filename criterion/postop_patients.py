from digipod.criterion.patients import PatientsInTimeFrame
from digipod.terminology.vocabulary import OMOP_SURGICAL_PROCEDURE
from execution_engine.omop.criterion.abstract import (
    SQL_ONE_SECOND,
    column_interval_type,
)
from execution_engine.util.interval import IntervalType
from sqlalchemy import Interval, func, select
from sqlalchemy.sql import Select


class PostOperativePatientsUntilDay0(PatientsInTimeFrame):
    """
    Select patients who are post-surgical in the timeframe between the day of the surgery and 6 days after the surgery.
    """

    postoperative_days = 0

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """
        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (func.date_trunc("day", self._table.c.procedure_end_datetime)).label(
                "interval_start"
            ),
            (
                func.date_trunc("day", self._table.c.procedure_end_datetime)
                + func.cast(func.concat(self.postoperative_days + 1, "day"), Interval)
                - SQL_ONE_SECOND
            ).label("interval_end"),
        ).where(self._table.c.procedure_concept_id == OMOP_SURGICAL_PROCEDURE)

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


class PostOperativePatientsUntilDay6(PostOperativePatientsUntilDay0):
    """
    Select patients who are post-surgical in the timeframe between the day of the surgery and 6 days after the surgery.
    """

    postoperative_days = 6
