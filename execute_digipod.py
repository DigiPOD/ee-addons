import logging
import os
import re
import sys

import pendulum
from sqlalchemy import text

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

os.environ["ENV_FILE"] = os.path.join(current_dir, "digipod.env")


from execution_engine.omop.vocabulary import standard_vocabulary

from digipod.vocabulary import DigiPOD

standard_vocabulary.register(DigiPOD)

from execution_engine.builder import ExecutionEngineBuilder
from execution_engine.clients import omopdb
from execution_engine.omop import cohort
from execution_engine.settings import get_config, update_config

import digipod

# enable multiprocessing with all available cores
# update_config(multiprocessing_use=False, multiprocessing_pool_size=-1)

# disable multiprocessing
update_config(multiprocessing_use=False)


result_schema = get_config().omop.db_result_schema

# Validate the schema name to ensure it's safe to use in the query
if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", result_schema):
    raise ValueError(f"Invalid schema name: {result_schema}")

# Optional: Truncate all tables before execution
with omopdb.begin() as con:
    schema_exists = (
        con.execute(
            text(
                "SELECT count(*) FROM information_schema.schemata WHERE schema_name = :schema_name;"
            ),
            {"schema_name": result_schema},
        ).fetchone()[0]
        > 0
    )

    # If the schema exists, proceed to truncate tables
    if schema_exists:
        con.execute(
            text(
                "TRUNCATE TABLE "
                f"   {result_schema}.comment, "
                f"   {result_schema}.recommendation, "
                f"   {result_schema}.criterion, "
                f"   {result_schema}.execution_run, "
                f"   {result_schema}.result_interval, "
                f"   {result_schema}.recommendation, "
                f"   {result_schema}.population_intervention_pair "
                "RESTART IDENTITY",
            )
        )


recommendation_package_version = "latest"

start_datetime = pendulum.parse("2020-01-01 00:00:00+01:00")
end_datetime = pendulum.parse("2023-05-31 23:59:59+01:00")


builder = ExecutionEngineBuilder()
# builder.set_characteristic_converters([VentilatorManagementAction])
# builder.set_action_converters([VentilatorManagementAction])
# builder.set_goal_converters([VentilatorManagementAction])

# Build the ExecutionEngine
engine = builder.build()

logging.getLogger().setLevel(logging.DEBUG)


# we'll rather build recommendations
# TODO: we need to register the recommendations in the database, if they haven't been registered!
recommendations: list[cohort.Recommendation] = [
    digipod.recommendation.recommendation_2_1.RecCollCheckRFAdultSurgicalPatientsPreoperatively,
    digipod.recommendation.recommendation_0_1.rec_0_1_Delirium_Screening,
]

# open questions
# - how do we check daily coverage? possibly as different PI pairs
# - values per shift should be determined by
#   - one criterion that gets the actual value
#   - shift criteria that are just valid for one shift per day (in principle we do not need sql for that, but the current
#     implementation of the Task.handle_criterion function always executes sql - we could change that
#  >> actually the problem is that these criteria would be valid for 8 hours and NO_DATA or NEGATIVE for the rest, and
#     we don't have a method to determine temporal counts (i.e. >= two out of three non-overlapping events)
#     thus, I think we need shift-value criteria, that check if the value is there within a timeframe (the shift) and
#     then set the whole day as POSITIVE or NEGATIVE -> then we can handle 2 out of 3 per day
# todo: - make a definitive overview of how intervals are combined within P, I, and between P&I and across PI pairs
#       - documentation on how to make custom criteria
#       - possibly: add a per-shift "extension" to criteria that just checks filters value inside time frames ?
#           -> implications have to be thought through
#       - implement rec2.1 and 0.1, 0.2
#       - run these

for recommendation in recommendations:
    print(recommendation.name)
    engine.register_recommendation(recommendation)
    engine.execute(
        recommendation, start_datetime=start_datetime, end_datetime=end_datetime
    )
