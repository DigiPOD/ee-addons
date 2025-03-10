from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.util.value import Value

from digipod import concepts

NUDESC_documented = PointInTimeCriterion(
    concept=concepts.NuDESC,
    override_value_required=False,
    forward_fill=False,
)
DRS_documented = PointInTimeCriterion(
    concept=concepts.DRS,
    override_value_required=False,
    forward_fill=False,
)
DOS_documented = PointInTimeCriterion(
    concept=concepts.DOS,
    override_value_required=False,
    forward_fill=False,
)
CAM_documented = PointInTimeCriterion(
    concept=concepts.CAM,
    override_value_required=False,
    forward_fill=False,
)
AT4_documented = PointInTimeCriterion(
    concept=concepts.FourAT,
    override_value_required=False,
    forward_fill=False,
)
TDCAM_documented = PointInTimeCriterion(
    concept=concepts.ThreeDCAM,
    override_value_required=False,
    forward_fill=False,
)

CAMICU_documented = PointInTimeCriterion(
    concept=concepts.CAM_ICU,
    override_value_required=False,
    forward_fill=False,
)

DDS_documented = PointInTimeCriterion(
    concept=concepts.DDS,
    override_value_required=False,
    forward_fill=False,
)

ICDSC_documented = PointInTimeCriterion(
    concept=concepts.ICDSC,
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
