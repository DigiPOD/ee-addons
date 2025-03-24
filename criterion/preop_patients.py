from execution_engine.omop.criterion.abstract import column_interval_type
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import VisitOccurrence
from execution_engine.util import logic
from execution_engine.util.interval import IntervalType
from execution_engine.util.value.value import ValueScalar
from sqlalchemy import Interval, func, select
from sqlalchemy.sql import Select

from digipod import concepts
from digipod.criterion.patients import AdultPatients, SurgicalPatients


class PreOperativePatientsBeforeDayOfSurgery(SurgicalPatients):
    """
    Select patients who are pre-surgical in the timeframe between 42 days before the surgery and the day of the surgery.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        subquery = self._query_first_surgery()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (
                func.date_trunc("day", subquery.c.procedure_datetime)
                - func.cast(func.concat(42, "day"), Interval)
            ).label("interval_start"),
            (
                func.date_trunc("day", subquery.c.procedure_datetime)
                - func.cast(func.concat(1, "day"), Interval)
            ).label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first procedure per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query


# todo: potentially we need to require VISIT_DETAIL here
class PreAdmissionPatients(VisitOccurrence):
    """
    Select patients who have a pre-admission visit ("vorstationär").
    """

    def __init__(self) -> None:
        super().__init__(
            concept=concepts.OutpatientVisit,
        )


class InpatientPatients(VisitOccurrence):
    """
    Select patients who have an inpatient visit ("normalstationär").
    """

    def __init__(self) -> None:
        super().__init__(
            concept=concepts.InpatientVisit,
        )


class IntensiveCarePatients(VisitOccurrence):
    """
    Select patients who have an intensive care visit
    """

    def __init__(self) -> None:
        super().__init__(
            concept=concepts.IntensiveCare,
        )


MMSElt3 = PointInTimeCriterion(
    concept=concepts.MMSE,
    value=ValueScalar(value_max=2),
)


class PreOperativePatientsBeforeEndOfSurgery(SurgicalPatients):
    """
    Select patients who are pre-operative in the timeframe between 42 days before the surgery and the end of the surgery.
    """

    _max_days_before_surgery: int

    def __init__(
        self,
        max_days_before_surgery: int = 42,
    ) -> None:
        super().__init__()
        self._max_days_before_surgery = max_days_before_surgery

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        subquery = self._query_first_surgery()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (
                func.date_trunc("day", subquery.c.procedure_datetime)
                - func.cast(func.concat(self._max_days_before_surgery, "day"), Interval)
            ).label("interval_start"),
            subquery.c.procedure_end_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first procedure per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query


class PreOperativePatientsBeforeSurgery(SurgicalPatients):
    """
    Select patients who are pre-operative in the timeframe between 42 days before the surgery and the end of the surgery.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        subquery = self._query_first_surgery()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (
                func.date_trunc("day", subquery.c.procedure_datetime)
                - func.cast(func.concat(42, "day"), Interval)
            ).label("interval_start"),
            subquery.c.procedure_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first procedure per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query


"""
- >= 18 years
- 42 days until end of day before surgery
"""
preOperativeAdultBeforeDayOfSurgeryPatients = logic.And(
    AdultPatients(),
    PreOperativePatientsBeforeDayOfSurgery(),
)

"""
- >= 18 years
- 42 days until end of day before surgery
- MMSE >= 3
"""
preOperativeAdultBeforeDayOfSurgeryPatientsMMSElt3 = logic.And(
    AdultPatients(),
    PreOperativePatientsBeforeDayOfSurgery(),
    MMSElt3,
)


"""
- vorstationär OR normalstationär
"""
preAdmissionOrInpatientPatients = logic.Or(
    PreAdmissionPatients(),
    InpatientPatients(),
)

"""
- >= 18 years
- 42 days before day of surgery until end of surgery
- vorstationär OR normalstationär
"""
adultPatientsPreoperativelyGeneralOnSurgeryDayAndBefore = logic.And(
    AdultPatients(),
    PreOperativePatientsBeforeEndOfSurgery(),
    preAdmissionOrInpatientPatients,
)
