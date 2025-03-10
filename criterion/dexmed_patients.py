from typing import List

from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.abstract import (
    Criterion,
    column_interval_type,
    observation_end_datetime,
    observation_start_datetime,
)
from execution_engine.omop.criterion.combination.combination import CriterionCombination
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    FixedWindowTemporalIndicatorCombination,
    TemporalIndicatorCombination,
)
from execution_engine.omop.criterion.drug_exposure import DrugExposure
from execution_engine.util.interval import IntervalType
from sqlalchemy import select
from sqlalchemy.sql import Select

from digipod import concepts
from digipod.criterion.patients import FirstDexmedetomidineAdministration

drugDexmedetomidine = DrugExposure(
    ingredient_concept=concepts.Dexmedetomidine,
    dose=None,
    route=None,
)


def temporal_filter_criteria(
    criteria: List[Criterion | CriterionCombination],
    filter_: Criterion | CriterionCombination,
    category: CohortCategory = CohortCategory.POPULATION,
) -> list[TemporalIndicatorCombination]:
    """
    Filters each criterion in criteria individually and then returns an "AnyTime" TemporalCombination,
    meaning a single interval spanning the whole observed time, either POSITIVE if there is any
    POSITIVE criterion after filtering, otherwise negative
    """
    return [
        FixedWindowTemporalIndicatorCombination.AnyTime(
            LogicalCriterionCombination.And(c, filter_),
        )
        for c in criteria
    ]


class PatientsBeforeFirstDexAdministration(FirstDexmedetomidineAdministration):
    """
    Select patients in the timeframe before the first Dexmedetomidine administration.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for the time period before Dexmedetomidine administration.
        """

        subquery = self._query_first_dexmedetomidine()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            observation_start_datetime.label("interval_start"),
            subquery.c.drug_exposure_start_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first administration per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query


class PatientsAfterFirstDexAdministration(FirstDexmedetomidineAdministration):
    """
    Select patients in the timeframe after the first Dexmedetomidine administration.
    """

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for the time period after Dexmedetomidine administration.
        """

        subquery = self._query_first_dexmedetomidine()

        query = select(
            subquery.c.person_id,
            column_interval_type(IntervalType.POSITIVE),
            subquery.c.drug_exposure_start_datetime.label("interval_start"),
            observation_end_datetime.label("interval_end"),
        ).where(
            subquery.c.rn == 1
        )  # Filter only the first administration per person

        query = self._filter_base_persons(query, c_person_id=subquery.c.person_id)
        query = self._filter_datetime(query)

        return query
