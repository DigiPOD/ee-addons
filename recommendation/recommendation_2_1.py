from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination import CriterionCombination
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.omop.vocabulary import SNOMEDCT, standard_vocabulary

from digipod.criterion.preop_patients import PreOperativeAdultBeforeDayOfSurgeryPatients
from digipod.recommendation import package_version
from digipod.vocabulary import DigiPOD

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

ageDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "424144002"
    ),  # $sct#424144002 "Current chronological age (observable entity)"
    override_value_required=False,
)

# $sct#302132005 "American Society of Anesthesiologists physical status class (observable entity)"
asaDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "302132005"
    ),  # $sct#424144002 "Current chronological age (observable entity)"
    override_value_required=False,
)

#  $cs-digipod#009 "Result of Charlson Comorbidity Index"
cciDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "009"
    ),  # $cs-digipod#009 "Result of Charlson Comorbidity Index"
    override_value_required=False,
)

#  $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
miniCogDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "713408000"
    ),  # $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
    override_value_required=False,
)

#############
# PI Pairs
#############

_RecPlanCheckRiskFactorsAgeASACCIMiniCog = PopulationInterventionPair(
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
        operator=CriterionCombination.Operator(CriterionCombination.Operator.OR),
        category=CohortCategory.INTERVENTION,
        criteria=[ageDocumented, asaDocumented, cciDocumented, miniCogDocumented],
    ),
)

#############################
# Recommendation collections
#############################
RecCollCheckRFAdultSurgicalPatientsPreoperatively = Recommendation(
    pi_pairs=[_RecPlanCheckRiskFactorsAgeASACCIMiniCog],
    base_criterion=base_criterion,
    name="CheckRFAdultSurgicalPatientsPreoperatively",
    title="Check Risk Factors in Adult Surgical Patients Preoperatively",
    url="",
    version="0.1",
    description="Check Risk Factors in Adult Surgical Patients Preoperatively",
    recommendation_id=None,
    package_version=package_version,
)
