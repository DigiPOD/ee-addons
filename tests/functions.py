import datetime

from execution_engine.omop.db.omop.tables import (
    ConditionOccurrence,
    DrugExposure,
    Measurement,
    Observation,
    Person,
    ProcedureOccurrence,
    VisitDetail,
    VisitOccurrence,
)

from tests._testdata import concepts


def create_person(gender_concept_id: int, birth_date: datetime.date) -> Person:
    return Person(
        gender_concept_id=gender_concept_id,
        year_of_birth=birth_date.year,
        month_of_birth=birth_date.month,
        day_of_birth=birth_date.day,
        birth_datetime=datetime.datetime.combine(
            birth_date, datetime.datetime.min.time()
        ),
        ethnicity_concept_id=0,
        race_concept_id=0,
    )


def create_visit(
    person_id: int,
    visit_start_datetime: datetime.datetime,
    visit_end_datetime: datetime.datetime,
    visit_concept_id: int,
) -> VisitOccurrence:
    """
    Create a visit for a person (one single encounter)
    """
    return VisitOccurrence(
        person_id=person_id,
        visit_start_date=visit_start_datetime.date(),
        visit_start_datetime=visit_start_datetime,
        visit_end_date=visit_end_datetime.date(),
        visit_end_datetime=visit_end_datetime,
        visit_concept_id=visit_concept_id,
        visit_type_concept_id=concepts.VISIT_TYPE_STILL_PATIENT,
    )


def create_visit_detail(
    vo: VisitOccurrence,
    visit_detail_start_datetime: datetime.datetime,
    visit_detail_end_datetime: datetime.datetime,
    visit_detail_concept_id: int,
) -> VisitDetail:
    """
    Create a visit detail for a person (e.g. transfer between units in the hospital)
    """
    return VisitDetail(
        person_id=vo.person_id,
        visit_detail_concept_id=visit_detail_concept_id,
        visit_detail_start_date=visit_detail_start_datetime.date(),
        visit_detail_start_datetime=visit_detail_start_datetime,
        visit_detail_end_date=visit_detail_end_datetime.date(),
        visit_detail_end_datetime=visit_detail_end_datetime,
        visit_detail_type_concept_id=concepts.EHR,
        visit_occurrence_id=vo.visit_occurrence_id,
    )


def create_condition(
    person_id: int,
    condition_concept_id: int,
    condition_start_datetime: datetime.datetime,
    condition_end_datetime: datetime.datetime,
) -> ConditionOccurrence:
    """
    Create a condition for a visit
    """
    return ConditionOccurrence(
        person_id=person_id,
        condition_concept_id=condition_concept_id,
        condition_start_date=condition_start_datetime.date(),
        condition_start_datetime=condition_start_datetime,
        condition_end_date=condition_end_datetime.date(),
        condition_end_datetime=condition_end_datetime,
        condition_type_concept_id=concepts.EHR,
    )


def create_drug_exposure(
    person_id: int,
    drug_concept_id: int,
    start_datetime: datetime.datetime,
    end_datetime: datetime.datetime,
    quantity: float,
    route_concept_id: int | None = None,
) -> DrugExposure:
    """
    Create a drug exposure for a visit
    """
    assert (
        start_datetime <= end_datetime
    ), "drug_exposure: start_datetime must be before end_datetime"

    return DrugExposure(
        person_id=person_id,
        drug_concept_id=drug_concept_id,
        drug_exposure_start_datetime=start_datetime,
        drug_exposure_start_date=start_datetime.date(),
        drug_exposure_end_datetime=end_datetime,
        drug_exposure_end_date=end_datetime.date(),
        quantity=quantity,
        drug_type_concept_id=concepts.EHR,
        route_concept_id=route_concept_id,
    )


def create_measurement(
    person_id: int,
    measurement_concept_id: int,
    measurement_datetime: datetime.datetime,
    value_as_number: float | None = None,
    value_as_concept_id: int | None = None,
    unit_concept_id: int | None = None,
) -> Measurement:
    """
    Create a measurement for a visit
    """
    return Measurement(
        person_id=person_id,
        measurement_concept_id=measurement_concept_id,
        measurement_date=measurement_datetime.date(),
        measurement_datetime=measurement_datetime,
        value_as_number=value_as_number,
        value_as_concept_id=value_as_concept_id,
        unit_concept_id=unit_concept_id,
        measurement_type_concept_id=concepts.EHR,
    )


def create_observation(
    person_id: int,
    observation_concept_id: int,
    observation_datetime: datetime.datetime,
    value_as_number: float | None = None,
    value_as_string: str | None = None,
    value_as_concept_id: int | None = None,
    unit_concept_id: int | None = None,
) -> Observation:
    """
    Create an observation for a visit
    """
    return Observation(
        person_id=person_id,
        observation_concept_id=observation_concept_id,
        observation_date=observation_datetime.date(),
        observation_datetime=observation_datetime,
        observation_type_concept_id=concepts.EHR,
        value_as_number=value_as_number,
        value_as_string=value_as_string,
        value_as_concept_id=value_as_concept_id,
        unit_concept_id=unit_concept_id,
    )


def create_procedure(
    person_id: int,
    procedure_concept_id: int,
    start_datetime: datetime.datetime,
    end_datetime: datetime.datetime,
) -> ProcedureOccurrence:
    """
    Create a procedure for a visit
    """
    assert (
        start_datetime <= end_datetime
    ), "procedure: start_datetime must be before end_datetime"

    return ProcedureOccurrence(
        person_id=person_id,
        procedure_concept_id=procedure_concept_id,
        procedure_type_concept_id=concepts.EHR,
        procedure_date=start_datetime.date(),
        procedure_datetime=start_datetime,
        procedure_end_date=end_datetime.date(),
        procedure_end_datetime=end_datetime,
    )
