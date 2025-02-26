from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.combination import CriterionCombination
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    FixedWindowTemporalIndicatorCombination,
    TemporalIndicatorCombination,
)


def MorningShift(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Morning shift overlap
    """
    return FixedWindowTemporalIndicatorCombination.MorningShift(criterion)


def AfternoonShift(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Afternoon shift overlap
    """
    return FixedWindowTemporalIndicatorCombination.AfternoonShift(criterion)


def NightShift(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Night shift overlap
    """
    return FixedWindowTemporalIndicatorCombination.NightShift(criterion)


def NightShiftBeforeMidnight(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Night shift (before midnight) overlap
    """
    return FixedWindowTemporalIndicatorCombination.NightShiftBeforeMidnight(criterion)


def NightShiftAfterMidnight(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Night shift overlap
    """
    return FixedWindowTemporalIndicatorCombination.NightShiftAfterMidnight(criterion)


def Day(criterion: Criterion | CriterionCombination) -> TemporalIndicatorCombination:
    """
    Full Day Overlap
    """
    return FixedWindowTemporalIndicatorCombination.Day(criterion)


def AtLeast(
    *args: Criterion | CriterionCombination, threshold: int
) -> LogicalCriterionCombination:
    """
    At least threshold of the criteria must be met
    """
    return LogicalCriterionCombination.AtLeast(*args, threshold=threshold)


def AnyTime(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Any time overlap
    """
    return FixedWindowTemporalIndicatorCombination.AnyTime(criterion)
