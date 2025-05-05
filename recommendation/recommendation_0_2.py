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
from digipod.criterion.scores import *
from digipod.recommendation import package_version

#############
# criteria
#############
base_criterion = PatientsActiveDuringPeriod()

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

# gl 25-05-05: removed after email from Fatima (25-04-29):
# "Recommendation 0.1 und 0.2: Ortsgebundenes Delirscreening bitte raus.
# Wir bewerten vor der OP und nach der OP die Zeiträume."
# normalward_scores_filtered = logic.ConditionalFilter(
#     left=InpatientPatients(),
#     right=normalward_scores
# )
#
# icu_scores_filtered = logic.ConditionalFilter(
#     left=IntensiveCarePatients(),
#     right=icu_scores
# )
#
#scores = logic.Or(normalward_scores_filtered, icu_scores_filtered)

scores = logic.Or(normalward_scores, icu_scores)


pi_double_screening = PopulationInterventionPairExpr(
    name="RecCollDeliriumScreeningOnSurgeryDay",
    url="",
    base_criterion=base_criterion,
    population_expr=logic.And(
        AdultPatients(),
        PostOperativePatientsUntilDay5(),
    ),
    intervention_expr=logic.CappedMinCount(
        Day(NightShiftAfterMidnight(scores)),
        Day(MorningShift(scores)),
        Day(AfternoonShift(scores)),
        Day(NightShiftBeforeMidnight(scores)),
        threshold=2,
    ),
)

#############################
# Recommendation collections
#############################

rec_0_2_Delirium_Screening_double = Recommendation(
    expr=pi_double_screening,
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
