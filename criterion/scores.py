from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.util.value import Value

from digipod import concepts

NUDESC_documented = PointInTimeCriterion(
    concept=concepts.NURSING_DELIRIUM_SCREENING_SCALE_NU_DESC_SCORE,
    value_required=False,
    forward_fill=False,
)
DRS_documented = PointInTimeCriterion(
    concept=concepts.DELIRIUM_RATING_SCALE_SCORE,
    value_required=False,
    forward_fill=False,
)
DOS_documented = PointInTimeCriterion(
    concept=concepts.DELIRIUM_OBSERVATION_SCALE_SCORE,
    value_required=False,
    forward_fill=False,
)
CAM_documented = PointInTimeCriterion(
    concept=concepts.CONFUSION_ASSESSMENT_METHOD_SCORE,
    value_required=False,
    forward_fill=False,
)
AT4_documented = PointInTimeCriterion(
    concept=concepts.FourAT,
    value_required=False,
    forward_fill=False,
)
TDCAM_documented = PointInTimeCriterion(
    concept=concepts.THREE_MINUTE_DIAGNOSTIC_INTERVIEW_FOR_CAM_DEFINED_DELIRIUM_SCORE,
    value_required=False,
    forward_fill=False,
)

CAMICU_documented = PointInTimeCriterion(
    concept=concepts.CONFUSION_ASSESSMENT_METHOD_FOR_THE_INTENSIVE_CARE_UNIT_SCORE,
    value_required=False,
    forward_fill=False,
)

DDS_documented = PointInTimeCriterion(
    concept=concepts.DELIRIUM_DETECTION_SCORE_SCORE,
    value_required=False,
    forward_fill=False,
)

ICDSC_documented = PointInTimeCriterion(
    concept=concepts.INTENSIVE_CARE_DELIRIUM_SCREENING_CHECKLIST_SCORE,
    value_required=False,
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
        value_required=False,
        forward_fill=False,
        value=value,
    )
