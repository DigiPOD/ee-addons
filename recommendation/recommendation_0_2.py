from typing import Sequence, Union

from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair
from execution_engine.omop.criterion.abstract import Criterion
from execution_engine.omop.criterion.combination import CriterionCombination
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod

from digipod.criterion.preop_patients import PreOperativeAdultBeforeDayOfSurgeryPatients

base_criterion = PatientsActiveDuringPeriod()

p1 = PopulationInterventionPair(
    name="",
    url="",
    base_criterion=base_criterion,
    population=CriterionCombination(
        exclude=False,
        operator=CriterionCombination.Operator(CriterionCombination.Operator.AND),
        category=CohortCategory.POPULATION,
        criteria=[PreOperativeAdultBeforeDayOfSurgeryPatients()],
    ),
    intervention=CriterionCombination(
        exclude=False,
        operator=CriterionCombination.Operator(CriterionCombination.Operator.AND),
        category=CohortCategory.POPULATION,
        criteria=[PreOperativeAdultBeforeDayOfSurgeryPatients()],
    ),
)


class AtLeastTwo(CriterionCombination):
    """
    A criterion combination that requires at least two of the given criteria to be met.
    """

    def __init__(
        self, criteria: Sequence[Union[Criterion, CriterionCombination]]
    ) -> None:
        super().__init__(
            exclude=False,
            operator=CriterionCombination.Operator(
                CriterionCombination.Operator.AT_LEAST, threshold=2
            ),
            category=CohortCategory.POPULATION,
            criteria=criteria,
        )
