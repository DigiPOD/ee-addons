import datetime
import logging
import os
from contextlib import contextmanager
from urllib.parse import quote

import pandas as pd
import pytest
import sqlalchemy
from execution_engine.util.types.timerange import TimeRange
from sqlalchemy import create_engine, event, text
from sqlalchemy.orm.session import sessionmaker

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

TIMEZONE = "Europe/Berlin"


@contextmanager
def disable_postgres_trigger(conn):
    conn.execute(text("SET session_replication_role = 'replica';"))

    yield

    conn.execute(text("SET session_replication_role = 'origin';"))
    conn.commit()


@pytest.fixture(scope="session")
def db_setup():
    """Database Session for SQLAlchemy."""
    # late import to prevent settings object being initialized before the test (and thus using the wrong settings)
    from execution_engine.omop.db.base import (  # noqa: F401 -- do not remove - needed for sqlalchemy to work
        Base,
        metadata,
    )
    from execution_engine.omop.db.celida.schema import SCHEMA_NAME as CELIDA_SCHEMA_NAME
    from execution_engine.omop.db.omop.schema import SCHEMA_NAME as OMOP_SCHEMA_NAME

    pg_user = os.environ["CELIDA_EE_OMOP__USER"]
    pg_password = os.environ["CELIDA_EE_OMOP__PASSWORD"]
    pg_host = os.environ["CELIDA_EE_OMOP__HOST"]
    pg_port = os.environ["CELIDA_EE_OMOP__PORT"]
    pg_db = os.environ["CELIDA_EE_OMOP__DATABASE"]

    connection_str = f"postgresql+psycopg://{quote(pg_user)}:{quote(pg_password)}@{pg_host}:{pg_port}/{pg_db}"
    engine = create_engine(connection_str)

    @event.listens_for(engine, "connect")
    def set_timezone(dbapi_connection, connection_record) -> None:
        """
        Set the timezone for the database connection.
        """
        cursor = dbapi_connection.cursor()
        cursor.execute(
            "SELECT set_config('TIMEZONE', %(timezone)s, false)",
            {"timezone": TIMEZONE},
        )
        cursor.close()

    with engine.begin() as con:
        if not con.dialect.has_schema(con, CELIDA_SCHEMA_NAME):
            con.execute(sqlalchemy.schema.CreateSchema(CELIDA_SCHEMA_NAME))
        if not con.dialect.has_schema(con, OMOP_SCHEMA_NAME):
            con.execute(sqlalchemy.schema.CreateSchema(OMOP_SCHEMA_NAME))

        with disable_postgres_trigger(con):
            metadata.create_all(con)
            logger.info("Inserting test data into the database.")

            for table in [
                "concept",
                "concept_relationship",
                "concept_ancestor",
                "drug_strength",
            ]:
                df = pd.read_csv(
                    f"tests/_testdata/omop_cdm/{table}.csv.gz",
                    na_values=[""],
                    keep_default_na=False,
                )
                for c in df.columns:
                    if "_date" in c:
                        df[c] = pd.to_datetime(df[c])
                df.to_sql(
                    table, con, schema=OMOP_SCHEMA_NAME, if_exists="append", index=False
                )

    with engine.begin() as con:
        with disable_postgres_trigger(con):
            from digipod.terminology.vocabulary import DigiPOD

            for concept in DigiPOD.map.values():
                insert_stmt = text(
                    f"INSERT INTO {OMOP_SCHEMA_NAME}.concept ("  # nosec  -- we need to insert the schema name here
                    "concept_id, concept_name, domain_id, vocabulary_id, concept_class_id, standard_concept, concept_code, valid_start_date, valid_end_date, invalid_reason"
                    ") VALUES ("
                    ":concept_id, :concept_name, :domain_id, :vocabulary_id, :concept_class_id, :standard_concept, :concept_code, :valid_start_date, :valid_end_date, :invalid_reason"
                    ")"
                )
                con.execute(
                    insert_stmt,
                    {
                        "concept_id": concept.concept_id,
                        "concept_name": concept.concept_name,
                        "domain_id": concept.domain_id,
                        "vocabulary_id": concept.vocabulary_id,
                        "concept_class_id": concept.concept_class_id,
                        "standard_concept": concept.standard_concept,
                        "concept_code": concept.concept_code,
                        "valid_start_date": datetime.date(2024, 1, 1),
                        "valid_end_date": datetime.date(2099, 12, 31),
                        "invalid_reason": None,
                    },
                )

    yield sessionmaker(bind=engine, expire_on_commit=False)


def truncate_tables(connection, schema_name, table_names):
    for table_name in table_names:
        sql = text(f"TRUNCATE TABLE {schema_name}.{table_name} CASCADE;")
        connection.execute(sql)


@pytest.fixture(scope="function")
def db_session(db_setup):
    # late import to prevent settings object being initialized before the test (and thus using the wrong settings)
    from execution_engine.omop.db.celida.schema import SCHEMA_NAME as CELIDA_SCHEMA_NAME
    from execution_engine.omop.db.omop.schema import SCHEMA_NAME as OMOP_SCHEMA_NAME

    session = db_setup()
    try:
        yield session
    finally:
        # Rollback any active transaction in the test session
        session.rollback()

        with session.begin():
            # Truncate tables in the OMOP schema
            truncate_tables(
                session,
                OMOP_SCHEMA_NAME,
                ["person"],
            )

            # Truncate tables in the CELIDA schema
            truncate_tables(
                session,
                CELIDA_SCHEMA_NAME,
                ["recommendation", "execution_run", "population_intervention_pair"],
            )

        session.close()


@contextmanager
def celida_recommendation(
    db_session,
    observation_window: TimeRange,
    recommendation_id=12,
    run_id=34,
    pi_pair_id=56,
    criterion_id=78,
):
    # late import to prevent settings object being initialized before the test (and thus using the wrong settings)
    import execution_engine
    from execution_engine.omop.db.base import (  # noqa: F401 -- do not remove - needed for sqlalchemy to work
        Base,
        metadata,
    )
    from execution_engine.omop.db.celida.schema import SCHEMA_NAME as CELIDA_SCHEMA_NAME
    from execution_engine.omop.db.celida.tables import (
        Criterion,
        ExecutionRun,
        PopulationInterventionPair,
        Recommendation,
    )

    try:
        recommendation = Recommendation(
            recommendation_id=recommendation_id,
            recommendation_name="my_recommendation",
            recommendation_title="my_title",
            recommendation_url="https://example.com",
            recommendation_version="1.0",
            recommendation_package_version="1.0",
            recommendation_hash=hash("my_recommendation"),
            recommendation_json="{}".encode(),
            create_datetime=datetime.datetime.now(),
        )
        db_session.add(recommendation)
        db_session.commit()

        run = ExecutionRun(
            run_id=run_id,
            observation_start_datetime=observation_window.start,
            observation_end_datetime=observation_window.end,
            run_datetime=datetime.datetime.now(),
            recommendation_id=recommendation_id,
            engine_version=execution_engine.__version__,
        )
        db_session.add(run)
        db_session.commit()

        pi_pair = PopulationInterventionPair(
            pi_pair_id=pi_pair_id,
            recommendation_id=recommendation_id,
            pi_pair_url="https://example.com",
            pi_pair_name="my_pair",
            pi_pair_hash=hash("my_pair"),
        )
        db_session.add(pi_pair)
        db_session.commit()

        criterion = Criterion(
            criterion_id=criterion_id,
            criterion_description="my_description",
            criterion_hash=hash("my_criterion"),
        )
        db_session.add(criterion)
        db_session.commit()

        yield {
            "run_id": run_id,
            "recommendation_id": recommendation_id,
            "pi_pair_id": pi_pair_id,
            "criterion_id": criterion_id,
        }
    finally:
        db_session.rollback()  # rollback in case of exceptions
        db_session.execute(
            text(f'TRUNCATE TABLE "{CELIDA_SCHEMA_NAME}"."recommendation" CASCADE;')
        )
        db_session.execute(
            text(f'TRUNCATE TABLE "{CELIDA_SCHEMA_NAME}"."execution_run" CASCADE;')
        )
        db_session.execute(
            text(
                f'TRUNCATE TABLE "{CELIDA_SCHEMA_NAME}"."population_intervention_pair" CASCADE;'
            )
        )
        db_session.execute(
            text(f'TRUNCATE TABLE "{CELIDA_SCHEMA_NAME}"."criterion" CASCADE;')
        )
        db_session.commit()
