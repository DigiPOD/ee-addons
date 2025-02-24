import logging
import os
import re
import sys

import pendulum
from execution_engine.omop.criterion.factory import register_criterion_class
from sqlalchemy import text

from digipod.converter.condition import DigiPODConditionCharacteristic
from digipod.converter.evaluation_procedure import (
    AssessmentCharacteristicConverter,
    OtherActionConverter,
    ProcedureWithExplicitContextConverter,
)
from digipod.converter.time_from_event import SurgicalOperationDate

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

os.environ["ENV_FILE"] = os.path.join(current_dir, "digipod.env")


from execution_engine.omop.vocabulary import standard_vocabulary

from digipod.converter.age import AgeConverter
from digipod.terminology.vocabulary import DigiPOD

standard_vocabulary.register(DigiPOD)

from execution_engine.builder import default_execution_engine_builder
from execution_engine.clients import omopdb
from execution_engine.omop import cohort
from execution_engine.settings import get_config, update_config

import digipod.recommendation.recommendation_0_1
import digipod.recommendation.recommendation_0_2
import digipod.recommendation.recommendation_2_1
import digipod.recommendation.recommendation_3_2

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

start_datetime = pendulum.parse("2024-01-01 00:00:00+01:00")
end_datetime = pendulum.parse("2025-05-31 23:59:59+01:00")


from digipod.criterion.patients import AgeLimitPatient

register_criterion_class("AgeLimitPatient", AgeLimitPatient)


builder = default_execution_engine_builder()

builder.prepend_characteristic_converter(AgeConverter)
builder.prepend_characteristic_converter(AssessmentCharacteristicConverter)
builder.prepend_characteristic_converter(ProcedureWithExplicitContextConverter)
builder.prepend_characteristic_converter(DigiPODConditionCharacteristic)

builder.prepend_action_converter(OtherActionConverter)

builder.append_time_from_event_converter(SurgicalOperationDate)


# Build the ExecutionEngine
engine = builder.build()

logging.getLogger().setLevel(logging.DEBUG)


# we'll rather build recommendations
# TODO: we need to register the recommendations in the database, if they haven't been registered!
recommendations: list[cohort.Recommendation] = [
    # digipod.recommendation.recommendation_0_2.rec_0_2_Delirium_Screening_single,
    # digipod.recommendation.recommendation_0_2.rec_0_2_Delirium_Screening_double,
    # digipod.recommendation.recommendation_2_1.RecCollCheckRFAdultSurgicalPatientsPreoperatively,
    # digipod.recommendation.recommendation_0_1.rec_0_1_Delirium_Screening,
    digipod.recommendation.recommendation_3_2.RecCollCheckRFAdultSurgicalPatientsPreoperatively
]
base_url = "https://fhir.charite.de/digipod/"

urls = ["PlanDefinition/RecCollPreoperativeRFAssessmentAndOptimization"]  # rec 4.1


for recommendation_url in urls:
    print(recommendation_url)
    cdd = engine.load_recommendation(
        base_url + recommendation_url,
        recommendation_package_version=recommendation_package_version,
    )


#
# from digipod.criterion.dexmed_patients import drugDexmedetomidine
# for recommendation in recommendations:
#     print(recommendation.name)
#     #print(drugDexmedetomidine.id)
#     engine.register_recommendation(recommendation)
#     engine.execute(
#         recommendation, start_datetime=start_datetime, end_datetime=end_datetime
#     )
#     engine.register_recommendation(recommendation)
#     engine.execute(
#         recommendation, start_datetime=start_datetime, end_datetime=end_datetime
#     )
