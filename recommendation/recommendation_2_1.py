from execution_engine.constants import CohortCategory
from execution_engine.omop.cohort import PopulationInterventionPair, Recommendation
from execution_engine.omop.criterion.combination.logical import (
    LogicalCriterionCombination,
)
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.omop.vocabulary import SNOMEDCT, standard_vocabulary

from digipod.criterion.preop_patients import (
    preOperativeAdultBeforeDayOfSurgeryPatients,
    preOperativeAdultBeforeDayOfSurgeryPatientsMMSEgte3,
)
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

# $sct#1255891005 "Montreal Cognitive Assessment version 8.1 score (observable entity)"
mocaDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "1255891005"
    ),  # $sct#1255891005 "Montreal Cognitive Assessment version 8.1 score (observable entity)"
    override_value_required=False,
)

# $cs-digipod#012 "Result of Addenbrooke cognitive examination revised"
acerDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        DigiPOD.system_uri, "012"
    ),  # $cs-digipod#012 "Result of Addenbrooke cognitive examination revised"
    override_value_required=False,
)

# $sct#447316007 "Mini-mental state examination score (observable entity)"
mmseDocumented = PointInTimeCriterion(
    category=CohortCategory.INTERVENTION,
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "447316007"
    ),  # $sct#447316007 "Mini-mental state examination score (observable entity)"
    override_value_required=False,
)


#############
# PI Pairs
#############

_RecPlanCheckRiskFactorsAgeASACCIMiniCog = PopulationInterventionPair(
    name="RecPlanCheckRiskFactorsAgeASACCIMiniCog",
    url="",
    base_criterion=base_criterion,
    population=preOperativeAdultBeforeDayOfSurgeryPatients,
    intervention=LogicalCriterionCombination.Or(
        ageDocumented,
        asaDocumented,
        cciDocumented,
        miniCogDocumented,
        category=CohortCategory.INTERVENTION,
    ),
)

_RecPlanCheckRiskFactorsMoCAACERMMSE = PopulationInterventionPair(
    name="RecPlanCheckRiskFactorsMoCAACERMMSE",
    url="",
    base_criterion=base_criterion,
    population=preOperativeAdultBeforeDayOfSurgeryPatientsMMSEgte3,
    intervention=LogicalCriterionCombination.AtLeast(
        mocaDocumented,
        acerDocumented,
        mmseDocumented,
        threshold=1,
        category=CohortCategory.INTERVENTION,
    ),
)

#############################
# Recommendation collections
#############################
RecCollCheckRFAdultSurgicalPatientsPreoperatively = Recommendation(
    pi_pairs=[
        _RecPlanCheckRiskFactorsAgeASACCIMiniCog,
        _RecPlanCheckRiskFactorsMoCAACERMMSE,
    ],
    base_criterion=base_criterion,
    name="CheckRFAdultSurgicalPatientsPreoperatively",
    title="Check Risk Factors in Adult Surgical Patients Preoperatively",
    url="",
    version="0.1",
    description="Check Risk Factors in Adult Surgical Patients Preoperatively",
    package_version=package_version,
)
