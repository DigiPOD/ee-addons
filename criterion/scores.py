from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.util.value import Value

from digipod import concepts

NUDESC_documented = PointInTimeCriterion(
    concept=concepts.NuDESC,
    value_required=False,
    forward_fill=False,
)
DRS_documented = PointInTimeCriterion(
    concept=concepts.DRS,
    value_required=False,
    forward_fill=False,
)
DOS_documented = PointInTimeCriterion(
    concept=concepts.DOS,
    value_required=False,
    forward_fill=False,
)
CAM_documented = PointInTimeCriterion(
    concept=concepts.CAM,
    value_required=False,
    forward_fill=False,
)
AT4_documented = PointInTimeCriterion(
    concept=concepts.FourAT,
    value_required=False,
    forward_fill=False,
)
TDCAM_documented = PointInTimeCriterion(
    concept=concepts.ThreeDCAM,
    value_required=False,
    forward_fill=False,
)

CAMICU_documented = PointInTimeCriterion(
    concept=concepts.CAM_ICU,
    value_required=False,
    forward_fill=False,
)

DDS_documented = PointInTimeCriterion(
    concept=concepts.DDS,
    value_required=False,
    forward_fill=False,
)

ICDSC_documented = PointInTimeCriterion(
    concept=concepts.ICDSC,
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
