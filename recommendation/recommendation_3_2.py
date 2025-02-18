from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod

from digipod.criterion.dexmed_patients import (
    popAdultPatientsIntraOrPostOPWithDexmedetomidineAndBradyOrHypo,
    popAdultPatWithDementiaGettingDexmedetomidineIntraOrPostOP,
    popAdultPatWithoutDementiaGettingDexmedetomidineIntraOrPostOP,
)
from digipod.criterion.noop import Noop
from digipod.recommendation import package_version

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

#############
# PI Pairs
#############

_recPlan_Dexmed_WithoutDementia = PopulationInterventionPair(
    name="RecPlanBalanceBenefitsAgainstSideEffectsWhenUsingDexmedetomidineInPatientWithoutDementia",
    url="",
    base_criterion=base_criterion,
    population=popAdultPatWithoutDementiaGettingDexmedetomidineIntraOrPostOP,
    intervention=LogicalCriterionCombination.And(
        Noop(category=CohortCategory.INTERVENTION), category=CohortCategory.INTERVENTION
    ),
)

_recPlan_Dexmed_WithDementia = PopulationInterventionPair(
    name="RecPlanBalanceBenefitsAgainstSideEffectsWhenUsingDexmedetomidineInPatientWithDementia",
    url="",
    base_criterion=base_criterion,
    population=popAdultPatWithDementiaGettingDexmedetomidineIntraOrPostOP,
    intervention=LogicalCriterionCombination.And(
        Noop(category=CohortCategory.INTERVENTION), category=CohortCategory.INTERVENTION
    ),
)

_recPlan_Dexmed_SideEffects = PopulationInterventionPair(
    name="RecPlanProvideDexmedetomidineSideEffectsWarning",
    url="",
    base_criterion=base_criterion,
    population=popAdultPatientsIntraOrPostOPWithDexmedetomidineAndBradyOrHypo,
    intervention=LogicalCriterionCombination.And(
        Noop(category=CohortCategory.INTERVENTION), category=CohortCategory.INTERVENTION
    ),
)

#############################
# Recommendation collections
#############################
RecCollCheckRFAdultSurgicalPatientsPreoperatively = Recommendation(
    pi_pairs=[
        _recPlan_Dexmed_WithoutDementia,
        _recPlan_Dexmed_WithDementia,
        _recPlan_Dexmed_SideEffects,
    ],
    base_criterion=base_criterion,
    name="Rec 3.2: BalanceBenefitsAgainstSideEffectsWhenUsingDexmedetomidine",
    title="Recommendation 3.2: Balance Benefits Against Side Effects When Using Dexmedetomidine",
    url="",
    version="0.3.0",
    description="Balance benefits against most expected side effects when administering dexmedetomidine in 'General Adult Surgical Patients Getting Dexmedetomidine Intra or Postoperatively to Prevent POD' or provide a warning in ''General Adult Surgical Patients Getting Dexmedetomidine Intra or Postoperatively to Prevent POD despite having or developing bradycardia and/or hypotension''",
    package_version=package_version,
)
