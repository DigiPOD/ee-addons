from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair
from execution_engine.omop.criterion.combination import CriterionCombination
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod

from digipod.criterion.postop_patients import PostOperativePatientsUntilDay6

base_criterion = PatientsActiveDuringPeriod()

##############################
# Day0
##############################


p1 = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDayMorningShift",
    url="",
    base_criterion=base_criterion,
    population=CriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        category=CohortCategory.POPULATION,
    ),
    intervention=CriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        category=CohortCategory.POPULATION,
    ),
)

p2 = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDayEveningShift",
    url="",
    base_criterion=base_criterion,
    population=CriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        category=CohortCategory.POPULATION,
    ),
    intervention=CriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        category=CohortCategory.POPULATION,
    ),
)

p2 = PopulationInterventionPair(
    name="RecCollDeliriumScreeningOnSurgeryDayNightShift",
    url="",
    base_criterion=base_criterion,
    population=CriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        category=CohortCategory.POPULATION,
    ),
    intervention=CriterionCombination.And(
        PostOperativePatientsUntilDay6(),
        category=CohortCategory.POPULATION,
    ),
)
