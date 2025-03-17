from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.point_in_time import PointInTimeCriterion
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.omop.vocabulary import SNOMEDCT, standard_vocabulary
from execution_engine.util import logic, temporal_logic_util

from digipod.criterion.preop_patients import (
    preOperativeAdultBeforeDayOfSurgeryPatients,
    preOperativeAdultBeforeDayOfSurgeryPatientsMMSEgte3,
)
from digipod.recommendation import package_version
from digipod.terminology import vocabulary

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

ageDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "424144002"
    ),  # $sct#424144002 "Current chronological age (observable entity)"
    value_required=False,
)

# $sct#302132005 "American Society of Anesthesiologists physical status class (observable entity)"
asaDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(SNOMEDCT.system_uri, "302132005"),
    value_required=False,
)

#  $cs-digipod#009 "Result of Charlson Comorbidity Index"
cciDocumented = PointInTimeCriterion(
    concept=vocabulary.RESULT_OF_CHARLSON_COMORBIDITY_INDEX,
    value_required=False,
)

#  $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
miniCogDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "713408000", standard=False
    ),  # $sct#713408000 "Mini-Cog brief cognitive screening test score (observable entity)"
    value_required=False,
)

# $sct#1255891005 "Montreal Cognitive Assessment version 8.1 score (observable entity)"
mocaDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "1255891005"
    ),  # $sct#1255891005 "Montreal Cognitive Assessment version 8.1 score (observable entity)"
    value_required=False,
)

# $sct-uk#711061000000109 "Addenbrooke's cognitive examination revised - score (observable entity)"
acerDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "711061000000109", standard=False
    ),  # $sct-uk#711061000000109 "Addenbrooke's cognitive examination revised - score (observable entity)"
    value_required=False,
)

# $sct#447316007 "Mini-mental state examination score (observable entity)"
mmseDocumented = PointInTimeCriterion(
    concept=standard_vocabulary.get_concept(
        SNOMEDCT.system_uri, "447316007", standard=False
    ),  # $sct#447316007 "Mini-mental state examination score (observable entity)"
    value_required=False,
)


#############
# PI Pairs
#############

_RecPlanCheckRiskFactorsAgeASACCIMiniCog = PopulationInterventionPairExpr(
    name="RecPlanCheckRiskFactorsAgeASACCIMiniCog",
    url="",
    base_criterion=base_criterion,
    population_expr=preOperativeAdultBeforeDayOfSurgeryPatients,
    intervention_expr=temporal_logic_util.AnyTime(
        logic.Or(
            ageDocumented,
            asaDocumented,
            cciDocumented,
            miniCogDocumented,
        ),
    ),
)

_RecPlanCheckRiskFactorsMoCAACERMMSE = PopulationInterventionPairExpr(
    name="RecPlanCheckRiskFactorsMoCAACERMMSE",
    url="",
    base_criterion=base_criterion,
    population_expr=preOperativeAdultBeforeDayOfSurgeryPatientsMMSEgte3,
    intervention_expr=temporal_logic_util.AnyTime(
        logic.MinCount(
            mocaDocumented,
            acerDocumented,
            mmseDocumented,
            threshold=1,
        ),
    ),
)

#############################
# Recommendation collections
#############################
RecCollCheckRFAdultSurgicalPatientsPreoperatively = Recommendation(
    expr=logic.Or(
        _RecPlanCheckRiskFactorsAgeASACCIMiniCog,
        _RecPlanCheckRiskFactorsMoCAACERMMSE,
    ),
    base_criterion=base_criterion,
    name="Rec 2.1: CheckRFAdultSurgicalPatientsPreoperatively",
    title="Recommendation 2.1: Check risk factors in 'General Adult Surgical Patients' Preoperatively",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollCheckRFAdultSurgicalPatientsPreoperatively",
    version="0.2.0",
    description="Adult patients before undergoing a surgical intervention of any type independently of the type of anesthesia: "
    "Check risk factors age, American Society of Anesthesiology Physical status score (ASA), "
    "Charlson Comorbidity Index (CCI) and Mini-cog test score (Mini-cog). "
    "If Mini-cog test score is equal to or higher than 3, perform Montreal Cognitive Assessment (MoCA), A"
    "ddenbrooke's Cognitive Examination (ACE-R) or Mini Mental State Examination (MMSE). "
    "Please note that MMSE is not free of charge (license fees)",
    package_version=package_version,
)
