import datetime
from abc import ABC

from dateutil.relativedelta import relativedelta
from execution_engine.omop.criterion.abstract import (
    Criterion,
    column_interval_type,
    observation_end_datetime,
    observation_start_datetime,
)
from execution_engine.omop.db.omop.tables import (
    DrugExposure,
    Person,
    ProcedureOccurrence,
)
from execution_engine.omop.vocabulary import OMOP_SURGICAL_PROCEDURE
from execution_engine.util.interval import IntervalType
from sqlalchemy import func, select
from sqlalchemy.sql import Select

from digipod.concepts import Dexmedetomidine


class AgeLimitPatient(Criterion):
    """
    Select patients who are at least 18 years old.
    """

    _static = True
    _min_age_years: int

    def __init__(
        self,
        min_age_years: int = 18,
    ) -> None:
        super().__init__()
        self._table = Person.__table__.alias("p")
        self._min_age_years = min_age_years

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return "AdultPatients"

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """
        # Current date minus 18 years to find the maximum birth date for 18-year-olds
        eighteen_years_ago = datetime.datetime.now() - relativedelta(
            years=self._min_age_years
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


class AdultPatients(AgeLimitPatient):
    """
    Select patients who are at least 18 years old.
    """

    def __init__(self) -> None:
        super().__init__(min_age_years=18)


class PatientsInTimeFrame(Criterion):
    """
    Select patients who are pre-surgical in the timeframe between 42 days before the surgery and the day of the surgery.
    """

    _static = True

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return self.__class__.__name__


class SurgicalPatients(PatientsInTimeFrame, ABC):
    """
    Select first surgery per patient
    """

    def __init__(self) -> None:
        super().__init__()
        self._table = ProcedureOccurrence.__table__.alias("po")

    def _query_first_surgery(self) -> Select:
        subquery = (
            select(
                self._table.c.person_id,
                self._table.c.procedure_occurrence_id,
                self._table.c.procedure_datetime,
                self._table.c.procedure_end_datetime,
                func.row_number()
                .over(
                    partition_by=self._table.c.person_id,
                    order_by=self._table.c.procedure_datetime,
                )
                .label("rn"),
            )
            .where(self._table.c.procedure_concept_id == OMOP_SURGICAL_PROCEDURE)
            .alias("first_procedure")
        )

        return subquery


class FirstDexmedetomidineAdministration(PatientsInTimeFrame):
    """
    Select first administration of Dexmedetomidine per patient.
    """

    def __init__(self) -> None:
        super().__init__()
        self._table = DrugExposure.__table__.alias("d")

    def _query_first_dexmedetomidine(self) -> Select:
        subquery = (
            select(
                self._table.c.person_id,
                self._table.c.drug_exposure_id,
                self._table.c.drug_exposure_start_datetime,
                self._table.c.drug_exposure_end_datetime,
                func.row_number()
                .over(
                    partition_by=self._table.c.person_id,
                    order_by=self._table.c.drug_exposure_start_datetime,
                )
                .label("rn"),
            )
            .where(self._table.c.drug_concept_id == Dexmedetomidine.concept_id)
            .alias("first_dexmedetomidine")
        )

        return subquery
