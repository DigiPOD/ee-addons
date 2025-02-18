from execution_engine.omop.criterion.abstract import column_interval_type
from execution_engine.util.interval import IntervalType
from sqlalchemy import select
from sqlalchemy.sql import Select

from digipod.criterion.patients import SurgicalPatients


class IntraOperativePatients(SurgicalPatients):
    """
    Select patients who are post-surgical in the timeframe between the day of the surgery and 6 days after the surgery.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        subquery = self._query_first_surgery()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            subquery.c.procedure_datetime.label("interval_start"),
            subquery.c.procedure_end_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first procedure per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query
