import inspect
import logging
import os
import re
import sys
import time
from collections import OrderedDict
from types import ModuleType
from typing import Generator, Type

import pendulum
from sqlalchemy import text

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

os.environ["ENV_FILE"] = os.path.join(current_dir, "digipod.env")


from execution_engine.omop.vocabulary import standard_vocabulary

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
import digipod.recommendation.recommendation_4_1
import digipod.recommendation.recommendation_4_2
import digipod.recommendation.recommendation_4_3

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


def iterate_module_classes(module: ModuleType) -> Generator[Type, None, None]:
    """
    Yields all classes listed in the `__all__` attribute of a module.

    :param module: The module from which to import classes.
    :return: A generator yielding classes defined in the module's `__all__` list.
    """

    if hasattr(module, "__all__"):
        for class_name in module.__all__:
            cls = getattr(module, class_name, None)
            if inspect.isclass(cls):
                yield cls


builder = default_execution_engine_builder()

import digipod.converter.action
import digipod.converter.characteristic
import digipod.converter.relative_time
import digipod.converter.time_from_event
import digipod.criterion

logging.getLogger().setLevel(logging.DEBUG)


for cls in iterate_module_classes(digipod.converter.characteristic):
    logging.info(f'Importing characteristic converter "{cls.__name__}"')
    builder.prepend_characteristic_converter(cls)

for cls in iterate_module_classes(digipod.converter.action):
    logging.info(f'Importing action converter "{cls.__name__}"')
    builder.prepend_action_converter(cls)

for cls in iterate_module_classes(digipod.converter.time_from_event):
    logging.info(f'Importing timeFromEvent converter "{cls.__name__}"')
    builder.append_time_from_event_converter(cls)

for cls in iterate_module_classes(digipod.converter.relative_time):
    logging.info(f'Importing relativeTime converter "{cls.__name__}"')
    builder.append_relative_time_converter(cls)


# Build the ExecutionEngine
engine = builder.build()

recommendations: list[cohort.Recommendation] = [
    # digipod.recommendation.recommendation_0_2.rec_0_2_Delirium_Screening_single,
    # digipod.recommendation.recommendation_0_2.rec_0_2_Delirium_Screening_double,
    # digipod.recommendation.recommendation_2_1.RecCollCheckRFAdultSurgicalPatientsPreoperatively,
    # digipod.recommendation.recommendation_0_1.rec_0_1_Delirium_Screening,
    digipod.recommendation.recommendation_3_2.recommendation,
    # digipod.recommendation.recommendation_4_1.recommendation,
    # digipod.recommendation.recommendation_4_2.recommendation,
    # digipod.recommendation.recommendation_4_3.recommendation,
]

base_url = "https://fhir.charite.de/digipod/"
urls: dict[str, str] = OrderedDict()

# manually implemented
# urls["0.1"] = "PlanDefinition/RecCollPreoperativeDeliriumScreening"
# urls["0.2"] = "PlanDefinition/RecCollDeliriumScreeningPostoperatively"
# urls["2.1"] = "PlanDefinition/RecCollCheckRFAdultSurgicalPatientsPreoperatively"
# urls["3.2"] = (
#     "PlanDefinition/RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE"
# )

# priority
# urls["4.1"] = "PlanDefinition/RecCollPreoperativeRFAssessmentAndOptimization"
# urls["4.2"] = (
#     "PlanDefinition/RecCollShareRFOfOlderAdultsPreOPAndRegisterPreventiveStrategies"  # works
# )
# urls["4.3"] = (
#     "PlanDefinition/RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD"
# )

# unknown
# urls["3.1"] = "PlanDefinition/RecCollAdultSurgicalPatNoSpecProphylacticDrugForPOD"
# urls["3.3"] = (
#     "PlanDefinition/RecCollAdultSurgicalPatPreOrIntraOPNoSpecSurgeryOrAnesthesiaType"
# )
# urls["3.4"] = "PlanDefinition/RecCollAdultSurgicalPatPreOrIntraOPNoSpecificBiomarker"
# urls["5.1"] = "PlanDefinition/RecCollIntraoperativeEEGMonitoringDepth"
# urls["5.2"] = "PlanDefinition/RecCollIntraoperativeMultiparameterEEG"
# urls["6.2"] = "PlanDefinition/RecCollBenzoTreatmentofDeliriumInAdultSurgicalPatPostoperatively"
# urls["6.3"] = "PlanDefinition/RecCollAdministerDexmedetomidineToPostOPCardiacSurgeryPatForPOD"

import pathlib

path = pathlib.Path("recommendation/gen")
assert path.exists()

header = """from digipod.criterion import PatientsBeforeFirstDexAdministration
from digipod.criterion.intraop_patients import IntraOperativePatients
from digipod.criterion.patients import AgeLimitPatient
from digipod.criterion.preop_patients import PreOperativePatientsBeforeSurgery, PreOperativePatientsBeforeDayOfSurgery
from digipod.criterion import PostOperativePatients, OnFacesAnxietyScaleAssessmentDay, \
    BeforeDailyFacesAnxietyScaleAssessment
from execution_engine.omop.cohort import Recommendation, PopulationInterventionPairExpr
from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.condition_occurrence import ConditionOccurrence
from execution_engine.omop.criterion.drug_exposure import DrugExposure
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.criterion.device_exposure import DeviceExposure
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.enum import TimeUnit
from execution_engine.util.logic import *
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept, ValueScalar
from execution_engine.util.value.time import ValueCount


"""

for rec_no, recommendation_url in urls.items():
    print(rec_no, recommendation_url)
    recommendation = engine.load_recommendation(
        base_url + recommendation_url,
        recommendation_package_version=recommendation_package_version,
    )

    with open(path / f"rec_{rec_no.replace('.', '_')}.py", "w") as f:
        f.write(header)
        f.write("recommendation = " + repr(recommendation))

    # engine.execute(
    #     recommendation, start_datetime=start_datetime, end_datetime=end_datetime
    # )

start_time = time.time()

for recommendation in recommendations:
    print(recommendation.name)
    engine.register_recommendation(recommendation)
    engine.execute(
        recommendation, start_datetime=start_datetime, end_datetime=end_datetime
    )

end_time = time.time()
runtime_seconds = end_time - start_time

logging.info(f"Total runtime: {runtime_seconds:.2f} seconds")
