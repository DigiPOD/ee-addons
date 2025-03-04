from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.vocabulary import standard_vocabulary
from execution_engine.util.value import Value

from digipod.concepts import FourAT
from digipod.terminology.vocabulary import DigiPOD

NUDESC_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "016"
    ),  # $cs-digipod#016 "Nursing Delirium Screening Scale (NU-DESC) score"
    override_value_required=False,
    forward_fill=False,
)
DRS_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "019"
    ),  # $cs-digipod#019 "Delirium Rating Scale score"
    override_value_required=False,
    forward_fill=False,
)
DOS_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "020"
    ),  # $cs-digipod#020 "Delirium Observation Scale score"
    override_value_required=False,
    forward_fill=False,
)
CAM_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "018"
    ),  # $cs-digipod#018 "Confusion Assessment Method score"
    override_value_required=False,
    forward_fill=False,
)
AT4_documented = PointInTimeCriterion(
    concept=FourAT,
    override_value_required=False,
    forward_fill=False,
)
TDCAM_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "021"
    ),  # $cs-digipod#021 "3-minute Diagnostic Interview for CAM-defined Delirium score"
    override_value_required=False,
    forward_fill=False,
)

CAMICU_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "022"
    ),  # $cs-digipod#022 "Confusion Assessment Method for the Intensive Care Unit score"
    override_value_required=False,
    forward_fill=False,
)

DDS_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "023"
    ),  # $cs-digipod#023 "Delirium Detection Score score"
    override_value_required=False,
    forward_fill=False,
)

ICDSC_documented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "024"
    ),  # $cs-digipod#024 "Intensive Care Delirium Screening Checklist score"
    override_value_required=False,
    forward_fill=False,
)


def score_threshold(
    concept: Concept,
    value: Value,
) -> PointInTimeCriterion:
    """
    Returns a PointInTime Criterion for the given Concept and Value
    """
    return PointInTimeCriterion(
        concept=concept,
        override_value_required=False,
        forward_fill=False,
        value=value,
    )
