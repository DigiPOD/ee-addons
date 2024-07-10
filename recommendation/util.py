from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination.combination import CriterionCombination
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.combination.temporal import (
    TemporalIndicatorCombination,
)


def MorningShift(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Morning shift overlap
    """
    return TemporalIndicatorCombination.MorningShift(
        criterion, category=CohortCategory.INTERVENTION
    )


def AfternoonShift(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Afternoon shift overlap
    """
    return TemporalIndicatorCombination.AfternoonShift(
        criterion, category=CohortCategory.INTERVENTION
    )


def NightShift(
    criterion: Criterion | CriterionCombination,
) -> TemporalIndicatorCombination:
    """
    Night shift overlap
    """
    return TemporalIndicatorCombination.NightShift(
        criterion, category=CohortCategory.INTERVENTION
    )


def Day(criterion: Criterion | CriterionCombination) -> TemporalIndicatorCombination:
    """
    Full Day Overlap
    """
    return TemporalIndicatorCombination.Day(
        criterion, category=CohortCategory.INTERVENTION
    )


def AtLeast(
    *args: Criterion | CriterionCombination, threshold: int
) -> LogicalCriterionCombination:
    """
    At least threshold of the criteria must be met
    """
    return LogicalCriterionCombination.AtLeast(
        *args, threshold=threshold, category=CohortCategory.INTERVENTION
    )
