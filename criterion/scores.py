from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.vocabulary import standard_vocabulary

from digipod.terminology.vocabulary import DigiPOD

NUDESC_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "016"
    ),  # $cs-digipod#016 "Nursing Delirium Screening Scale (NU-DESC) score"
    override_value_required=False,
)
DRS_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "019"
    ),  # $cs-digipod#019 "Delirium Rating Scale score"
    override_value_required=False,
)
DOS_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "020"
    ),  # $cs-digipod#020 "Delirium Observation Scale score"
    override_value_required=False,
)
CAM_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "018"
    ),  # $cs-digipod#018 "Confusion Assessment Method score"
    override_value_required=False,
)
AT4_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "017"
    ),  # $cs-digipod#017 "4AT score"
    override_value_required=False,
)
TDCAM_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "021"
    ),  # $cs-digipod#021 "3-minute Diagnostic Interview for CAM-defined Delirium score"
    override_value_required=False,
)

CAMICU_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "022"
    ),  # $cs-digipod#022 "Confusion Assessment Method for the Intensive Care Unit score"
    override_value_required=False,
)

DDS_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "023"
    ),  # $cs-digipod#023 "Delirium Detection Score score"
    override_value_required=False,
)

ICDSC_documented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "024"
    ),  # $cs-digipod#024 "Intensive Care Delirium Screening Checklist score"
    override_value_required=False,
)
