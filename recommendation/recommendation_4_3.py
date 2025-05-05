from functools import reduce

from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.task.process import IntervalWithCount
from execution_engine.task.task import Task
from execution_engine.util.interval import IntervalType
from execution_engine.util.temporal_logic_util import AnyTime, Day
from execution_engine.util.types import PersonIntervals

from digipod.criterion import PostOperativePatientsUntilDay5
from digipod.criterion.non_pharma_measures import *

#######################################################################################################################
PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery = And(AnyTime(anyHighRiskForDelirium), PostOperativePatientsUntilDay5())


class MaxCountOr(logic.Or):
    """
    A logical Or operation that returns the maximum interval_count of all intervals
    of the highest priority type.
    """

    @staticmethod
    def count_intervals(start: int, end: int, intervals: list[IntervalWithCount | None]
                        ) -> IntervalWithCount:
        """
        Combines two intervals into a single IntervalWithCount.

        This function is used as a callback in `process.find_rectangles`.
        """
        result_type = None
        result_count = 0

        for interval in intervals:
            if interval is None:
                interval_type, interval_count = IntervalType.NEGATIVE, 0
            else:
                interval_type, interval_count = interval.type, cast(int, interval.count)

            if (
                    (
                            interval_type is IntervalType.POSITIVE
                            and result_type is not IntervalType.POSITIVE
                    )
                    or (
                    interval_type is IntervalType.NO_DATA
                    and result_type is not IntervalType.POSITIVE
                    and result_type is not IntervalType.NO_DATA
            )
                    or (
                    interval_type is IntervalType.NEGATIVE
                    and (result_type is IntervalType.NOT_APPLICABLE or result_type is None)
            )
                    or (interval_type is IntervalType.NOT_APPLICABLE and result_type is None)
            ):
                result_type = interval_type
                result_count = 0
            result_count = max(result_count, interval_count)
        return IntervalWithCount(start, end, result_type, result_count)

###################################################
# BUNDLE 1 - Anxiety
#####################################################
bundle_anxiety = MinCount( # 100% wenn erfüllt, 0 % wenn nicht
    PopulationInterventionPairExpr(
        population_expr=And(
        PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
            #Not(AnyTime(anyDementiaBeforeDayOfSurgery)), # gl 25-05-05: removed after email from Fatima (25-04-29): "Demenz bitte rausnehmen"
        ),
        intervention_expr=Day(facesAnxietyScoreAssessed),
        name="RecPlanAssessFASPostoperatively",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanAssessFASPostoperatively",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    # Apr-14, 2025 (email Laerson Hoff): Angst: Es muss nur noch der FAS dokumentiert werden. Eine Bewertung der
    # Angstbewältigung ist nicht mehr erforderlich. Mit anderen Worten: Dieser Teil der Empfehlung gilt als
    # erfüllt, sobald der FAS dokumentiert wurde. Dies soll einmal täglich nach der Operation erfolgen.
    # PopulationInterventionPairExpr(
    #     population_expr=And(
    #         AnyTime(anyHighRiskForDelirium),
    #         Or(AnyTime(anyDementiaBeforeSurgery), Day(anyPositiveDeliriumTest)),
    #         PostOperativePatientsUntilDay5()
    #     ),
    #     intervention_expr=And(
    #         Day(nonPharmaAnxietyIntervention),
    #         Or(
    #             Day(verbalAnxietyManagement),
    #             Day(triggerAvoidanceForAnxiety),
    #             Day(socialServiceInterview),
    #             Day(palliativeCareConsultation),
    #             Day(familyInvolvementInCare),
    #             Day(individualizedPatientEducation),
    #             Day(identificationOfCarePreferences),
    #         ),
    #     ),
    #     name="RecPlanNonPharmaAnxietyMeasuresInPatWithDementiaOrDeliriumPostOP",
    #     url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaAnxietyMeasuresInPatWithDementiaOrDeliriumPostOP",
    #     base_criterion=PatientsActiveDuringPeriod(),
    # ),
    # PopulationInterventionPairExpr(
    #     population_expr=And(
    #         PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
    #         Not(AnyTime(anyDementiaBeforeDayOfSurgery)),
    #         Day(Or(
    #             PreFacesScalePostOp(nudescLt2),
    #             PreFacesScalePostOp(nudescNegative),
    #             PreFacesScalePostOp(nudescWeaklyPositive),
    #             PreFacesScalePostOp(icdscLt4),
    #             PreFacesScalePostOp(icdscNegative),
    #             PreFacesScalePostOp(icdscWeaklyPositive),
    #             PreFacesScalePostOp(camNegative),
    #             PreFacesScalePostOp(drsLt12),
    #             PreFacesScalePostOp(drsNegative),
    #             PreFacesScalePostOp(drsWeaklyPositive),
    #             PreFacesScalePostOp(dosLt3),
    #             PreFacesScalePostOp(dosNegative),
    #             PreFacesScalePostOp(dosWeaklyPositive),
    #             PreFacesScalePostOp(tdcamNegative),
    #             PreFacesScalePostOp(camicuNegative),
    #             PreFacesScalePostOp(ddsLt8),
    #             PreFacesScalePostOp(ddsNegative),
    #             PreFacesScalePostOp(ddsWeaklyPositive),
    #             PreFacesScalePostOp(FourAtLt4),
    #             PreFacesScalePostOp(FourAtNegative),
    #             PreFacesScalePostOp(FourAtWeaklyPositive),
    #         )),
    #         Day(Or(
    #             Not(PreFacesScaleOnAssessmentDayPostOp(nudescGte2)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(nudescPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(icdscGte4)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(icdscPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(camPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(drsGte12)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(drsPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(dosGte3)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(dosPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(tdcamPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(camicuPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(ddsGte7)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(ddsPositive)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(FourAtGte4)),
    #             Not(PreFacesScaleOnAssessmentDayPostOp(FourAtPositive)),
    #         )),
    #         Day(facesAnxietyScoreGte2),
    #     ),
    #     intervention_expr=MinCount(
    #         OnFacesScaleAssessmentDayPostOp(nonPharmaAnxietyIntervention),
    #         Or(
    #             OnFacesScaleAssessmentDayPostOp(verbalAnxietyManagement),
    #             OnFacesScaleAssessmentDayPostOp(triggerAvoidanceForAnxiety),
    #             OnFacesScaleAssessmentDayPostOp(socialServiceInterview),
    #             OnFacesScaleAssessmentDayPostOp(palliativeCareConsultation),
    #             OnFacesScaleAssessmentDayPostOp(familyInvolvementInCare),
    #             OnFacesScaleAssessmentDayPostOp(individualizedPatientEducation),
    #             OnFacesScaleAssessmentDayPostOp(
    #                 identificationOfCarePreferences
    #             ),
    #         ),
    #         threshold=1
    #     ),
    #     name="RecPlanNonPharmaMeasuresForAnxietyInPatWithPositiveFASPostOP",
    #     url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaMeasuresForAnxietyInPatWithPositiveFASPostOP",
    #     base_criterion=PatientsActiveDuringPeriod(),
    # ),
    threshold=1,
)

#####################################################
# BUNDLE 2 - Cognition
#####################################################
bundle_cognition = MinCount( # 100% wenn mind. 1 erfüllt, sonst 0
    PopulationInterventionPairExpr(
        population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
        intervention_expr=MinCount(
            Day(cognitiveStimulationProcedure),
            # gl 25-30-31: commented out because this is equivalent to the above, and Laerson didn't map these
            # Or(
            #     Day(readingActivity),
            #     Day(conversationForCognition),
            #     Day(boardGamesOrPuzzles),
            #     Day(singingActivity),
            #     Day(cognitiveAssessment),
            # ),
            threshold=1,
        ),
        name="RecPlanCognitiveStimulationPostOP",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanCognitiveStimulationPostOP",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    # todo: should start at the actual day where this is provided
    PopulationInterventionPairExpr(
        population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
        intervention_expr=MinCount(
            Day(communicationAidProvision),
            # gl 25-30-31: commented out because this is equivalent to the above, and Laerson didn't map these
            # Or(
            #     PostOperative(spectacleSupply),
            #     PostOperative(hearingAidProvision),
            #     PostOperative(assistiveWritingDevice),
            #     PostOperative(removableDentureProvision),
            #     PostOperative(interpreterServiceRequest),
            #     PostOperative(communicationAssistiveDevice),
            # ),
            threshold=1,
        ),
        name="RecPlanProvisionOfCommunicationAidsPostOP",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanProvisionOfCommunicationAidsPostOP",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    PopulationInterventionPairExpr(
        population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
        intervention_expr=MinCount(
            Day(supportCircadianRhythm),
            # gl 25-30-31: commented out because this is equivalent to the above, and Laerson didn't map these
            # Or(
            #     Day(sleepingMaskProvision),
            #     Day(earplugsAtNight),
            #     Day(noiseReduction),
            #     Day(lightExposureDaytime),
            #     Day(reduceNightLight),
            #     Day(closePatientRoomDoor),
            #     Day(promoteSleepHygiene),
            #     Day(onlyEmergencyAtNight),
            #     Day(otherSleepHygieneInterventions),
            # ),
            threshold=1,
        ),
        name="RecPlanNonPharmaInterventionsSupportingCircardianRhythmPostOP",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaInterventionsSupportingCircardianRhythmPostOP",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    # todo: should start at the actual day where this is provided
    PopulationInterventionPairExpr(
        population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
        intervention_expr=MinCount(
            Day(realityOrientation),
            # gl 25-30-31: commented out because this is equivalent to the above, and Laerson didn't map these
            # Or(
            #     PostOperative(wearableWatch),
            #     PostOperative(calendarDevice),
            #     PostOperative(printedMaterial),
            #     PostOperative(televisionDevice),
            #     PostOperative(radioDevice),
            #     PostOperative(otherMediaExposure),
            # ),
            threshold=1,
        ),
        name="RecPlanDocumentProvisionOrientationAidPostOP",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentProvisionOrientationAidPostOP",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    threshold=1
)

#####################################################
# BUNDLE 3 - Mobilization
#####################################################
bundle_mobilization = CappedMinCount(
    PopulationInterventionPairExpr(
        population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
        intervention_expr=Day(mobilizationAbilityObservation),
        name="RecPlanDocumentMobilizationAbilitiesPostoperatively",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentMobilizationAbilitiesPostoperatively",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    PopulationInterventionPairExpr(
        population_expr=And(PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery, Day(doesNotMobilize)),
        intervention_expr=MinCount(
            Day(physiatricJointMobilization),
            Or(
                Day(contraindicationObservation),
                Day(patientNonCompliance),
                Day(lackOfEnergyCondition),
                Day(anxietyCondition),
                Day(painCondition),
                Day(exhaustionObservation),
                Day(dizzinessCondition),
                Day(reasonAndJustificationObservation),
            ),
            threshold=1,
        ),
        name="RecPlanDocumentMobilizePatientOrDocumentWhyNoMobilizationPostOP",
        url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentMobilizePatientOrDocumentWhyNoMobilizationPostOP",
        base_criterion=PatientsActiveDuringPeriod(),
    ),
    threshold=2,
)

#####################################################
# BUNDLE 4 - Feeding
#####################################################
bundle_feeding = MaxCountOr(
    #######################################################
    # Self Feeding
    #######################################################
CappedMinCount(
        PopulationInterventionPairExpr(
            population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
            intervention_expr=Day(selfFeedingAbility),
            name="RecPlanDocumentFeedingAbilitiesPostoperatively",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentFeedingAbilitiesPostoperatively",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
        PopulationInterventionPairExpr(
            population_expr=And(PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery, Day(doesNotFeedSelf)),
            intervention_expr=ExactCount(
                Day(enteralFeeding),
                Or(
                    Day(contraindicationObservation),
                    Day(ivFeeding),
                    Day(aspirationRisk),
                    Day(abnormalDeglutition),
                    Day(painCondition),
                    Day(lossOfAppetite),
                    Day(digestiveReflux),
                    Day(nauseaAndVomiting),
                ),
                threshold=1,
            ),
            name="RecPlanDocumentFeedEnterallyPatientOrDocumentWhyNoFeedingPostOP",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentFeedEnterallyPatientOrDocumentWhyNoFeedingPostOP",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
        threshold=2,
    ),
    #######################################################
    # Deglutition
    #######################################################
    CappedMinCount(
    PopulationInterventionPairExpr(
            population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
            intervention_expr=Day(deglutition),
            name="RecPlanDocumentDeglutitionAbilitiesPostoperatively",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentDeglutitionAbilitiesPostoperatively",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
        PopulationInterventionPairExpr(
            population_expr=And(PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery, Day(difficultySwallowing)),
            intervention_expr=Or(
                Day(dysphagiaTherapy),
                Day(nutritionalRegimeModification),
            ),
            name="RecPlanDeglutitionRelatedInterventionsPostoperatively",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDeglutitionRelatedInterventionsPostoperatively",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
        threshold=2,
    ),
    #######################################################
    # MouthCare
    #######################################################
    logic.MinCount( # encapsulate in MinCount so each child of the parent MaxCountOr is a count-type (required for
        # task.py to call the custom counting function of MaxCountOr
        PopulationInterventionPairExpr(
            population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
            intervention_expr=Day(mouthCareManagement),
            name="RecPlanOralCareRelatedInterventionsPostoperatively",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanOralCareRelatedInterventionsPostoperatively",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
        threshold=1,
    ),
)

class CombineRecommendation4_3(logic.And):
    """
    Combines the two distinct population/intervention pairs in this recommendation and calculates
    a weighted sum of the counts.
    """

    @staticmethod
    def prepare_data(task: Task, data: list[PersonIntervals]) -> list[PersonIntervals]:
        """
        Selects and returns the PersonIntervals in the order
        - result of bundle_anxiety
        - result of bundle_cognition
        - result of bundle_mobilization
        - result of bundle_feeding

        This function is used in task.Task to sort the incoming data such that the `count_intervals` function
        can rely on this order.
        """
        assert task.expr.args[0].args[0].name == bundle_anxiety.args[0].name
        assert task.expr.args[1].args[0].name == bundle_cognition.args[0].name
        assert task.expr.args[2].args[0].name == bundle_mobilization.args[0].name
        assert task.expr.args[3].args[0].args[0].name == bundle_feeding.args[0].args[0].name

        idx_anxiety = task.get_predecessor_data_index(task.expr.args[0])
        idx_cognition = task.get_predecessor_data_index(task.expr.args[1])
        idx_mobilization = task.get_predecessor_data_index(task.expr.args[2])
        idx_feeding = task.get_predecessor_data_index(task.expr.args[3])

        if len(data) != 4:
            raise ValueError('Expected exactly 4 inputs')

        return [
            data[idx_anxiety],
            data[idx_cognition],
            data[idx_mobilization],
            data[idx_feeding],
        ]


    @staticmethod
    def count_intervals(start: int, end: int, intervals: list[IntervalWithCount]
    ) -> IntervalWithCount:
        """
        Combines two intervals into a single IntervalWithCount, handling special cases.

        This function is used as a callback in `process.find_rectangles`.

        Due to ` prepare_data`, the intervals are expected to be (in that order):
        - index 0: result of _piScreeningOfRFInOlderPatientsPreOP
        - index 1: result of _piOptimizationOfPreOPStatusInOlderPatPreoperatively

        If the second interval is NOT_APPLICABLE - i.e. the patient is not part of the population of the second
        PI pair, the first interval is returned directly.
        Otherwise, a union of both intervals is created, and the count value is
        calculated based on the notion that there are 4 items to be fulfilled in
        _RecPlanCheckRiskFactorsAgeASACCIMiniCog, and 1 item in _RecPlanCheckRiskFactorsMoCAACERMMSE.
        Accordingly, a weighted count is calculated.
        """
        # we need to take special care, unfortunately, that:
        # - interval can be with or without count (if without, .count is the namedtuple build-in method)

        # todo: do we need to handle not_applicable?

        result_count = sum(interval.count if interval is not None else 0 for interval in intervals) / len(intervals)
        result_type = reduce(lambda x, y: x & y, (interval.type if interval else IntervalType.NEGATIVE for interval in intervals))
        return IntervalWithCount(start, end, result_type, result_count)


recommendation = Recommendation(
    expr=CombineRecommendation4_3(
        bundle_anxiety,
        bundle_cognition,
        bundle_mobilization,
        bundle_feeding,
    ),
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD",
    title="Recommendation Collection: Perform a bundle of non-pharmacological interventions once a day postoperatively in different populations of 'Adult Surgical Patients At Risk For POD'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD",
    version="0.1.0",
    description="Recommendation collection for different populations of adult patients that were at risk for postoperative delirium before undergoing a surgical intervention of any type independently of the type of anesthesia: Perform different non-pharmacological interventions (related to anxiety, nutrition, mobilization, and cognition) as bundle once a day postoperatively until discharge.",
    package_version="latest",
)
