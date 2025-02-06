from digipod import concepts
from digipod.concepts import OMOP_SURGICAL_PROCEDURE
from digipod.criterion.patients import AdultPatients, PatientsInTimeFrame
from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.abstract import column_interval_type
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import VisitOccurrence
from execution_engine.util.interval import IntervalType
from execution_engine.util.value import ValueNumber
from sqlalchemy import Interval, func, select
from sqlalchemy.sql import Select


class PreOperativePatientsBeforeDayOfSurgery(PatientsInTimeFrame):
    """
    Select patients who are pre-surgical in the timeframe between 42 days before the surgery and the day of the surgery.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

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
        ).where(self._table.c.procedure_concept_id == OMOP_SURGICAL_PROCEDURE)

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
            category=CohortCategory.POPULATION,
            concept=concepts.OutpatientVisit,
        )


class InpatientPatients(VisitOccurrence):
    """
    Select patients who have an inpatient visit ("normalstationär").
    """

    def __init__(self) -> None:
        super().__init__(
            category=CohortCategory.POPULATION,
            concept=concepts.InpatientVisit,
        )


class IntensiveCarePatients(VisitOccurrence):
    """
    Select patients who have an intensive care visit
    """

    def __init__(self) -> None:
        super().__init__(
            category=CohortCategory.POPULATION,
            concept=concepts.IntensiveCare,
        )


MMSEgte3 = PointInTimeCriterion(
    category=CohortCategory.POPULATION,
    concept=concepts.MMSE,
    value=ValueNumber(value_min=3, unit=concepts.unit_score),
)


class PreOperativePatientsBeforeEndOfSurgery(PatientsInTimeFrame):
    """
    Select patients who are pre-operative in the timeframe between 42 days before the surgery and the end of the surgery.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """

        query = select(
            self._table.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            (
                func.date_trunc("day", self._table.c.procedure_datetime)
                - func.cast(func.concat(42, "day"), Interval)
            ).label("interval_start"),
            self._table.c.procedure_end_datetime.label("interval_end"),
        ).where(self._table.c.procedure_concept_id == OMOP_SURGICAL_PROCEDURE)

        query = self._filter_base_persons(query)
        query = self._filter_datetime(query)

        return query


"""
- >= 18 years
- 42 days until end of day before surgery
"""
preOperativeAdultBeforeDayOfSurgeryPatients = LogicalCriterionCombination.And(
    AdultPatients(),
    PreOperativePatientsBeforeDayOfSurgery(),
    category=CohortCategory.POPULATION,
)

"""
- >= 18 years
- 42 days until end of day before surgery
- MMSE >= 3
"""
preOperativeAdultBeforeDayOfSurgeryPatientsMMSEgte3 = LogicalCriterionCombination.And(
    AdultPatients(),
    PreOperativePatientsBeforeDayOfSurgery(),
    MMSEgte3,
    category=CohortCategory.POPULATION,
)


"""
- vorstationär OR normalstationär
"""
preAdmissionOrInpatientPatients = LogicalCriterionCombination.Or(
    PreAdmissionPatients(),
    InpatientPatients(),
    category=CohortCategory.POPULATION,
)

"""
- >= 18 years
- 42 days before day of surgery until end of surgery
- vorstationär OR normalstationär
"""
adultPatientsPreoperativelyGeneralOnSurgeryDayAndBefore = (
    LogicalCriterionCombination.And(
        AdultPatients(),
        PreOperativePatientsBeforeEndOfSurgery(),
        preAdmissionOrInpatientPatients,
        category=CohortCategory.POPULATION,
    )
)
