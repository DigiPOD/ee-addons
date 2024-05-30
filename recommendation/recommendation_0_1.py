from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination import CriterionCombination
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.omop.vocabulary import standard_vocabulary

from digipod.criterion.preop_patients import preOperativePatientsBeforeEndOfSurgery
from digipod.recommendation import package_version
from digipod.vocabulary import DigiPOD

base_criterion = PatientsActiveDuringPeriod()

# $cs-digipod#016 "Nursing Delirium Screening Scale (NU-DESC) score"
NUDESC_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "016"
    ),  # $cs-digipod#016 "Nursing Delirium Screening Scale (NU-DESC) score"
    override_value_required=False,
)

# $cs-digipod#019 "Delirium Rating Scale score"
DRS_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "019"
    ),  # $cs-digipod#019 "Delirium Rating Scale score"
    override_value_required=False,
)

# $cs-digipod#020 "Delirium Observation Scale score"
DOS_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "020"
    ),  # $cs-digipod#020 "Delirium Observation Scale score"
    override_value_required=False,
)

# $cs-digipod#018 "Confusion Assessment Method score"
CAM_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "018"
    ),  # $cs-digipod#018 "Confusion Assessment Method score"
    override_value_required=False,
)

# $cs-digipod#017 "4AT score"
AT4_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "017"
    ),  # $cs-digipod#017 "4AT score"
    override_value_required=False,
)

# $cs-digipod#021 "3-minute Diagnostic Interview for CAM-defined Delirium score"
TDCAM_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "021"
    ),  # $cs-digipod#021 "3-minute Diagnostic Interview for CAM-defined Delirium score"
    override_value_required=False,
)


_RecPlanPreoperativeDeliriumScreening = PopulationInterventionPair(
    name="",
    url="",
    base_criterion=base_criterion,
    population=preOperativePatientsBeforeEndOfSurgery,
    intervention=CriterionCombination.AtLeast(
        NUDESC_documented,
        DRS_documented,
        DOS_documented,
        CAM_documented,
        AT4_documented,
        TDCAM_documented,
        threshold=1,
        category=CohortCategory.INTERVENTION,
    ),
)

rec_0_1_Delirium_Screening = Recommendation(
    pi_pairs=[_RecPlanPreoperativeDeliriumScreening],
    base_criterion=base_criterion,
    name="CheckRFAdultSurgicalPatientsPreoperatively",
    title="Check Risk Factors in Adult Surgical Patients Preoperatively",
    url="",
    version="0.1",
    description="Check Risk Factors in Adult Surgical Patients Preoperatively",
    package_version=package_version,
)
