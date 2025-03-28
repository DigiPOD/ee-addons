from execution_engine.omop.concepts import Concept
from execution_engine.omop.criterion.measurement import Measurement
from execution_engine.omop.criterion.observation import Observation
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.util.types import Timing
from execution_engine.util.value import ValueConcept

from digipod.terminology.custom_concepts import (
    OPTIMIZABLE_PREOPERATIVE_RISK_FACTOR,
    PREOPERATIVE_RISK_FACTOR_OPTIMIZATION,
)

snomedAssessmentRiskDelirium = Concept(
    concept_id=36676218,
    concept_name="Assessment for risk of delirium",
    domain_id="Procedure",
    vocabulary_id="SNOMED",
    concept_class_id="Procedure",
    standard_concept="S",
    concept_code="772787001",
    valid_start_date="2019-01-31",
    valid_end_date="2099-12-31",
    invalid_reason=None,
)

assessmentForRiskOfPostOperativeDelirium = ProcedureOccurrence(
    static=False,
    timing=None,
    concept=snomedAssessmentRiskDelirium,
    value=None,
)

cardiacAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4314723,
        concept_name="Cardiac assessment",
        concept_code="425315000",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

neurologicalAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4021179,
        concept_name="Neurological assessment",
        concept_code="225398001",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

cardiovascularEvaluation = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4181638,
        concept_name="Cardiovascular examination and evaluation",
        concept_code="43038000",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

diabetesScreening = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4064918,
        concept_name="Diabetes mellitus screening",
        concept_code="171183004",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
)

anemiaScreening = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4062491,
        concept_name="Anemia screening",
        concept_code="171201007",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
)

depressedMoodAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=46273905,
        concept_name="Assessment of depressed mood",
        concept_code="710846002",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

painAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4021323,
        concept_name="Pain assessment",
        concept_code="225399009",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

anxietyAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=46272472,
        concept_name="Assessment of anxiety",
        concept_code="710841007",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

substanceUseAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=762506,
        concept_name="Assessment of substance use",
        concept_code="428211000124100",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

cognitiveFunctionAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4012466,
        concept_name="Assessment and interpretation of higher cerebral function, cognitive testing",
        concept_code="113024001",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

dementiaAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=43021483,
        concept_name="Assessment of dementia",
        concept_code="473203000",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

frailtyAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4046889,
        concept_name="Frail elderly assessment",
        concept_code="134427001",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

sensoryImpairmentAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4158084,
        concept_name="Determination of existing sensory impairments",
        concept_code="370837004",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

nutritionalAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4149297,
        concept_name="Nutritional assessment",
        concept_code="310243009",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

medicationAdministrationAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4244831,
        concept_name="Medication administration assessment",
        concept_code="396073008",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

electrolytesMeasurement = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4193783,
        concept_name="Electrolytes measurement",
        concept_code="79301008",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
)

swallowingFunctionEvaluation = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4258123,
        concept_name="Evaluation of oral and pharyngeal swallowing function",
        concept_code="440363007",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

anticholinergicBurdenScale = Measurement(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=35621948,
        concept_name="Anticholinergic Cognitive Burden Scale",
        concept_code="763240001",
        domain_id="Measurement",
        vocabulary_id="SNOMED",
        concept_class_id="Staging / Scales",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
)

preAnestheticAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4057399,
        concept_name="Pre-anesthetic assessment",
        concept_code="182770003",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

dehydrationRiskAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=46272237,
        concept_name="Assessment of risk for dehydration",
        concept_code="710567009",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

impairedNutritionRiskAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=46272234,
        concept_name="Assessment of risk for impaired nutritional status",
        concept_code="710563008",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

hypovolemiaRiskAssessment = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=4155294,
        concept_name="Assessment of hypovolemia risk factors",
        concept_code="372114004",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

optimizablePreopRiskFactorPresent = Observation(
    static=False,
    value_required=False,
    concept=OPTIMIZABLE_PREOPERATIVE_RISK_FACTOR,
    forward_fill=True,
    value=ValueConcept(
        value={
            "concept_id": 4181412,
            "concept_name": "Present",
            "concept_code": "52101004",
            "domain_id": "Meas Value",
            "vocabulary_id": "SNOMED",
            "concept_class_id": "Qualifier Value",
            "standard_concept": "S",
            "invalid_reason": None,
        }
    ),
    timing=None,
)

preoperativeRiskFactorOptimization = Observation(
    static=False,
    value_required=False,
    concept=PREOPERATIVE_RISK_FACTOR_OPTIMIZATION,
    forward_fill=True,
    value=None,
    timing=None,
)

surgicalProcedure = ProcedureOccurrence(
    static=False,
    timing=None,
    concept=Concept(
        concept_id=4301351,
        concept_name="Surgical procedure",
        concept_code="387713003",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)

healthcareInformationExchange = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4296383,
        concept_name="Healthcare information exchange",
        concept_code="386317007",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
)

multidisciplinaryCareConference = Observation(
    static=False,
    value_required=False,
    concept=Concept(
        concept_id=4296791,
        concept_name="Multidisciplinary care conference",
        concept_code="384682003",
        domain_id="Observation",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    forward_fill=True,
    value=None,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
)

multidisciplinaryCaseManagement = ProcedureOccurrence(
    static=False,
    timing=Timing(
        count={"unit": None, "value": None, "value_min": 1, "value_max": None},
        duration=None,
        frequency=None,
        interval=None,
    ),
    concept=Concept(
        concept_id=44808908,
        concept_name="Multidisciplinary case management",
        concept_code="842901000000108",
        domain_id="Procedure",
        vocabulary_id="SNOMED",
        concept_class_id="Procedure",
        standard_concept="S",
        invalid_reason=None,
    ),
    value=None,
)
