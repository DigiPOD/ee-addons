from execution_engine.omop.criterion.abstract import column_interval_type
from execution_engine.util.interval import IntervalType
from sqlalchemy import Interval, func, select
from sqlalchemy.sql import Select

from digipod.criterion.patients import PatientsInTimeFrame


class PostOperativePatientsUntilDay6(PatientsInTimeFrame):
    """
    Select patients who are pre-surgical in the timeframe between 42 days before the surgery and the day of the surgery.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        # Define the concept ID for the surgical procedure
        surgical_procedure_concept_id = 4322976  # OMOP procedure

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (func.date_trunc("day", self._table.c.procedure_datetime)).label(
                "interval_start"
            ),
            (
                func.date_trunc("day", self._table.c.procedure_datetime)
                + func.cast(func.concat(6, "day"), Interval)
            ).label("interval_end"),
        ).where(self._table.c.procedure_concept_id == surgical_procedure_concept_id)

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query
