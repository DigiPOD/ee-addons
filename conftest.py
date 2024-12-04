import os
from glob import glob
from typing import Any

import pandas as pd
import pytest
from pytest_postgresql.janitor import DatabaseJanitor

# add each module in _fixtures as a pytest plugin (i.e. fixture)
pytest_plugins = [
    "digipod." + fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob("tests/_fixtures/[!__]*.py", recursive=True)
]


current_dir = os.path.dirname(__file__)
os.environ["ENV_FILE"] = os.path.join(current_dir, "digipod.env")


@pytest.fixture(autouse=True, scope="session")
def set_pandas_display_options() -> None:
    """
    Set the pandas display options for the entire test session.
    """
    pd.set_option("display.max_columns", 7)
    pd.set_option("display.width", 1000)


def postgres_janitor() -> DatabaseJanitor:
    """
    Create a janitor for postgresql.

    The janitor is used to create and destroy the database that is used in testing.

    :return: DatabaseJanitor
    """
    pg_user = os.environ["CELIDA_EE_OMOP__USER"]
    pg_pass = os.environ["CELIDA_EE_OMOP__PASSWORD"]
    pg_host = os.environ["CELIDA_EE_OMOP__HOST"]
    pg_port = os.environ["CELIDA_EE_OMOP__PORT"]
    pg_name = os.environ["CELIDA_EE_OMOP__DATABASE"]

    janitor = DatabaseJanitor(
        user=pg_user,
        host=pg_host,
        port=pg_port,
        dbname=pg_name,
        password=pg_pass,
        version="16",
        connection_timeout=5,
    )

    return janitor


def init_postgres(config):  # type: ignore
    """
    Initialize the postgres database.

    This function is called by pytest before the tests are run.
    - Set the environment variables that are used by the OMOPSQLClient
    - Drops the test database if it exists
    - Create the test database
    """

    def getvalue(name):  # type: ignore
        return config.getoption(name) or config.getini(name)

    os.environ["CELIDA_EE_OMOP__USER"] = getvalue("postgresql_user")
    os.environ["CELIDA_EE_OMOP__PASSWORD"] = getvalue("postgresql_password")
    os.environ["CELIDA_EE_OMOP__HOST"] = getvalue("postgresql_host")
    os.environ["CELIDA_EE_OMOP__PORT"] = str(getvalue("postgresql_port"))
    os.environ["CELIDA_EE_OMOP__DATABASE"] = getvalue("postgresql_dbname")

    janitor = postgres_janitor()

    # Drop the database if it already exists (e.g. from a previous interrupted test run)
    with janitor.cursor() as cur:
        db_exists = cur.execute(
            """SELECT EXISTS(
            SELECT datname FROM pg_catalog.pg_database WHERE datname = %(dbname)s
        )""",
            params={"dbname": getvalue("postgresql_dbname")},
        ).fetchone()[0]

    if db_exists:
        janitor.drop()

    janitor.init()


def pytest_sessionstart(session):  # type: ignore
    """
    Initialize the postgres database before the tests are run.
    """
    init_postgres(session.config)

    from execution_engine.omop.vocabulary import standard_vocabulary

    from digipod.terminology.vocabulary import DigiPOD

    standard_vocabulary.register(DigiPOD)


def pytest_sessionfinish(session):  # type: ignore
    """
    Drop the postgres database after the tests are run.
    """
    janitor = postgres_janitor()
    janitor.drop()


def pytest_assertrepr_compare(
    op: str,
    left: Any,
    right: Any,
) -> list[str] | None:
    """
    Custom pytest assertion comparison.
    """
    from digipod.tests.recommendation.resultset import ResultSet

    if isinstance(left, ResultSet) and isinstance(right, ResultSet) and op == "==":
        return left.comparison_report(right)

    return None
