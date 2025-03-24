from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util import logic
from execution_engine.util.temporal_logic_util import (
    AfternoonShift,
    Day,
    MorningShift,
    NightShiftAfterMidnight,
    NightShiftBeforeMidnight,
)

from digipod.criterion.patients import AdultPatients
from digipod.criterion.postop_patients import PostOperativePatientsUntilDay5
from digipod.criterion.preop_patients import InpatientPatients, IntensiveCarePatients
from digipod.criterion.scores import *
from digipod.recommendation import package_version

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

#############
# Day0
#############

#############
# PI Pairs
#############


normalward_scores = logic.Or(
    TDCAM_documented,  # 3DCAM Morning
    AT4_documented,  # AT4 Morning
    CAM_documented,  # CAM Morning
    DRS_documented,  # DRS Morning
    DOS_documented,  # DOS Morning
    NUDESC_documented,  # NuDESC Morning
)

icu_scores = logic.Or(
    CAMICU_documented,  # CAM ICU Morning
    DDS_documented,  # AT4 Morning
    ICDSC_documented,  # CAM Morning
)

pi_normalward_double_screening = PopulationInterventionPairExpr(
    name="RecCollDeliriumScreeningOnSurgeryDay_NormalWard",
    url="",
    base_criterion=base_criterion,
    population_expr=logic.And(
        AdultPatients(),
        PostOperativePatientsUntilDay5(),
        InpatientPatients(),
    ),
    intervention_expr=logic.CappedMinCount(
        Day(NightShiftAfterMidnight(normalward_scores)),
        Day(MorningShift(normalward_scores)),
        Day(AfternoonShift(normalward_scores)),
        Day(NightShiftBeforeMidnight(normalward_scores)),
        threshold=2,
    ),
)
#
# pi_normalward_single_screening = PopulationInterventionPairExpr(
#     name="RecCollDeliriumScreeningOnSurgeryDay_NormalWard",
#     url="",
#     base_criterion=base_criterion,
#     population_expr=logic.And(
#         AdultPatients(),
#         PostOperativePatientsUntilDay5(),
#         InpatientPatients(),
#     ),
#     intervention_expr=logic.CappedMinCount(
#         Day(NightShiftAfterMidnight(normalward_scores)),
#         Day(MorningShift(normalward_scores)),
#         Day(AfternoonShift(normalward_scores)),
#         Day(NightShiftBeforeMidnight(normalward_scores)),
#         threshold=1,
#     ),
# )


pi_icu_double_screening = PopulationInterventionPairExpr(
    name="RecCollDeliriumScreeningOnSurgeryDay_ICU",
    url="",
    base_criterion=base_criterion,
    population_expr=logic.And(
        AdultPatients(),
        PostOperativePatientsUntilDay5(),
        IntensiveCarePatients(),
    ),
    intervention_expr=logic.CappedMinCount(
        Day(NightShiftAfterMidnight(icu_scores)),
        Day(MorningShift(icu_scores)),
        Day(AfternoonShift(icu_scores)),
        Day(NightShiftBeforeMidnight(icu_scores)),
        threshold=2,
    ),
)

# pi_icu_single_screening = PopulationInterventionPairExpr(
#     name="RecCollDeliriumScreeningOnSurgeryDay_ICU",
#     url="",
#     base_criterion=base_criterion,
#     population_expr=logic.And(
#         AdultPatients(),
#         PostOperativePatientsUntilDay5(),
#         IntensiveCarePatients(),
#     ),
#     intervention_expr=logic.MinCount(
#         Day(NightShiftAfterMidnight(icu_scores)),
#         Day(MorningShift(icu_scores)),
#         Day(AfternoonShift(icu_scores)),
#         Day(NightShiftBeforeMidnight(icu_scores)),
#         threshold=1,
#     ),
# )


#############################
# Recommendation collections
#############################
# rec_0_2_Delirium_Screening_single = Recommendation(
#     expr=logic.Or(pi_normalward_single_screening, pi_icu_single_screening),
#     base_criterion=base_criterion,
#     name="Rec 0.2: PostoperativeDeliriumScreening (Single)",
#     title="Recommendation 0.2: Postoperative Screening of Delirium",
#     url="https://fhir.charite.de/digipod/PlanDefinition/RecCollDeliriumScreeningPostoperatively_single",
#     version="0.2.0",
#     description="Adult patients that had a surgical intervention of any type independently of the type of anesthesia: "
#     "Perform delirium screening from surgery day to the fifth postoperative day, "
#     "ideally once a shift and at least twice a day.",
#     package_version=package_version,
# )

rec_0_2_Delirium_Screening_double = Recommendation(
    expr=logic.Or(pi_normalward_double_screening, pi_icu_double_screening),
    base_criterion=base_criterion,
    name="Rec 0.2: PostoperativeDeliriumScreening (Double)",
    title="Recommendation 0.2: Postoperative Screening of Delirium",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollDeliriumScreeningPostoperatively",
    version="0.2.0",
    description="Adult patients that had a surgical intervention of any type independently of the type of anesthesia: "
    "Perform delirium screening from surgery day to the fifth postoperative day, "
    "ideally once a shift and at least twice a day.",
    package_version=package_version,
)
