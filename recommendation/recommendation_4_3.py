from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.temporal_logic_util import AnyTime, Day

from digipod.criterion import PostOperativePatientsUntilDay5
from digipod.criterion.non_pharma_measures import *

#######################################################################################################################
PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery = And(AnyTime(anyHighRiskForDelirium), PostOperativePatientsUntilDay5())

recommendation = Recommendation(
    expr=MinCount(
        #####################################################
        # BUNDLE 1 - Anxiety
        #####################################################
        And(
            PopulationInterventionPairExpr(
                population_expr=And(
                PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                    Not(AnyTime(anyDementiaBeforeDayOfSurgery)),
                ),
                intervention_expr=Day(facesAnxietyScoreAssessed),
                name="RecPlanAssessFASPostoperatively",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanAssessFASPostoperatively",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
            PopulationInterventionPairExpr(
                population_expr=And(
                    AnyTime(anyHighRiskForDelirium),
                    Or(AnyTime(anyDementiaBeforeSurgery), Day(anyPositiveDeliriumTest)),
                    PostOperativePatientsUntilDay5()
                ),
                intervention_expr=And(
                    Day(nonPharmaAnxietyIntervention),
                    Or(
                        Day(verbalAnxietyManagement),
                        Day(triggerAvoidanceForAnxiety),
                        Day(socialServiceInterview),
                        Day(palliativeCareConsultation),
                        Day(familyInvolvementInCare),
                        Day(individualizedPatientEducation),
                        Day(identificationOfCarePreferences),
                    ),
                ),
                name="RecPlanNonPharmaAnxietyMeasuresInPatWithDementiaOrDeliriumPostOP",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaAnxietyMeasuresInPatWithDementiaOrDeliriumPostOP",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
            PopulationInterventionPairExpr(
                population_expr=And(
                    PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                    Not(AnyTime(anyDementiaBeforeDayOfSurgery)),
                    Day(Or(
                        PreFacesScalePostOp(nudescLt2),
                        PreFacesScalePostOp(nudescNegative),
                        PreFacesScalePostOp(nudescWeaklyPositive),
                        PreFacesScalePostOp(icdscLt4),
                        PreFacesScalePostOp(icdscNegative),
                        PreFacesScalePostOp(icdscWeaklyPositive),
                        PreFacesScalePostOp(camNegative),
                        PreFacesScalePostOp(drsLt12),
                        PreFacesScalePostOp(drsNegative),
                        PreFacesScalePostOp(drsWeaklyPositive),
                        PreFacesScalePostOp(dosLt3),
                        PreFacesScalePostOp(dosNegative),
                        PreFacesScalePostOp(dosWeaklyPositive),
                        PreFacesScalePostOp(tdcamNegative),
                        PreFacesScalePostOp(camicuNegative),
                        PreFacesScalePostOp(ddsLt8),
                        PreFacesScalePostOp(ddsNegative),
                        PreFacesScalePostOp(ddsWeaklyPositive),
                        PreFacesScalePostOp(FourAtLt4),
                        PreFacesScalePostOp(FourAtNegative),
                        PreFacesScalePostOp(FourAtWeaklyPositive),
                    )),
                    Day(Or(
                        Not(PreFacesScaleOnAssessmentDayPostOp(nudescGte2)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(nudescPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(icdscGte4)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(icdscPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(camPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(drsGte12)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(drsPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(dosGte3)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(dosPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(tdcamPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(camicuPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(ddsGte7)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(ddsPositive)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(FourAtGte4)),
                        Not(PreFacesScaleOnAssessmentDayPostOp(FourAtPositive)),
                    )),
                    Day(facesAnxietyScoreGte2),
                ),
                intervention_expr=MinCount(
                    OnFacesScaleAssessmentDayPostOp(nonPharmaAnxietyIntervention),
                    Or(
                        OnFacesScaleAssessmentDayPostOp(verbalAnxietyManagement),
                        OnFacesScaleAssessmentDayPostOp(triggerAvoidanceForAnxiety),
                        OnFacesScaleAssessmentDayPostOp(socialServiceInterview),
                        OnFacesScaleAssessmentDayPostOp(palliativeCareConsultation),
                        OnFacesScaleAssessmentDayPostOp(familyInvolvementInCare),
                        OnFacesScaleAssessmentDayPostOp(individualizedPatientEducation),
                        OnFacesScaleAssessmentDayPostOp(
                            identificationOfCarePreferences
                        ),
                    ),
                    threshold=1
                ),
                name="RecPlanNonPharmaMeasuresForAnxietyInPatWithPositiveFASPostOP",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanNonPharmaMeasuresForAnxietyInPatWithPositiveFASPostOP",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
        ),
        #####################################################
        # BUNDLE 2 - Cognition
        #####################################################
        MinCount(
            PopulationInterventionPairExpr(
                population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                intervention_expr=MinCount(
                    Day(cognitiveStimulationProcedure),
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
                    PostOperative(communicationAidProvision),
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
                    PostOperative(realityOrientation),
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
            threshold=4
        ),
        #####################################################
        # BUNDLE 3 - Mobilization
        #####################################################
        And(
            PopulationInterventionPairExpr(
                population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                intervention_expr=Day(mobilizationAbilityObservation),
                name="RecPlanDocumentMobilizationAbilitiesPostoperatively",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentMobilizationAbilitiesPostoperatively",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
            PopulationInterventionPairExpr(
                population_expr=And(PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery, PostOperative(doesNotMobilize)),
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
        ),
        #####################################################
        # BUNDLE 4 - Feeding
        #####################################################
        And(
            PopulationInterventionPairExpr(
                population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                intervention_expr=Day(selfFeedingAbility),
                name="RecPlanDocumentFeedingAbilitiesPostoperatively",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentFeedingAbilitiesPostoperatively",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
            PopulationInterventionPairExpr(
                population_expr=And(PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery, PostOperative(doesNotFeedSelf)),
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
            PopulationInterventionPairExpr(
                population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                intervention_expr=Day(deglutition),
                name="RecPlanDocumentDeglutitionAbilitiesPostoperatively",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDocumentDeglutitionAbilitiesPostoperatively",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
            PopulationInterventionPairExpr(
                population_expr=And(PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery, difficultySwallowing),
                intervention_expr=And(
                    Day(dysphagiaTherapy),
                    PostOperative(nutritionalRegimeModification),
                ),
                name="RecPlanDeglutitionRelatedInterventionsPostoperatively",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanDeglutitionRelatedInterventionsPostoperatively",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
            PopulationInterventionPairExpr(
                population_expr=PostOperativePatientsWithHighRiskForDeliriumBeforeDayOfSurgery,
                intervention_expr=Day(mouthCareManagement),
                name="RecPlanOralCareRelatedInterventionsPostoperatively",
                url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanOralCareRelatedInterventionsPostoperatively",
                base_criterion=PatientsActiveDuringPeriod(),
            ),
        ),
        threshold=4,
    ),
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD",
    title="Recommendation Collection: Perform a bundle of non-pharmacological interventions once a day postoperatively in different populations of 'Adult Surgical Patients At Risk For POD'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollBundleOfNonPharmaMeasuresPostOPInAdultsAtRiskForPOD",
    version="0.1.0",
    description="Recommendation collection for different populations of adult patients that were at risk for postoperative delirium before undergoing a surgical intervention of any type independently of the type of anesthesia: Perform different non-pharmacological interventions (related to anxiety, nutrition, mobilization, and cognition) as bundle once a day postoperatively until discharge.",
    package_version="latest",
)
