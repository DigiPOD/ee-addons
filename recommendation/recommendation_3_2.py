from execution_engine.omop.cohort import PopulationInterventionPairExpr, Recommendation
from execution_engine.omop.criterion.abstract import Criterion, column_interval_type
from execution_engine.omop.criterion.procedure_occurrence import ProcedureOccurrence
from execution_engine.omop.criterion.visit_occurrence import PatientsActiveDuringPeriod
from execution_engine.util.interval import IntervalType
from execution_engine.util.logic import *
from execution_engine.util.temporal_logic_util import AnyTime
from sqlalchemy import Select, select

from digipod.concepts import Dexmedetomidine
from digipod.criterion.non_pharma_measures import (
    BeforeFirstDexAdministration,
    FourAtGte4,
    FourAtLt4,
    FourAtNegative,
    FourAtPositive,
    FourAtWeaklyPositive,
    IntraOrPostOperative,
    anyDementiaBeforeSurgery,
    camicuNegative,
    camicuPositive,
    camNegative,
    camPositive,
    ddsGte7,
    ddsLt8,
    ddsNegative,
    ddsPositive,
    ddsWeaklyPositive,
    dosGte3,
    dosLt3,
    dosNegative,
    dosPositive,
    dosWeaklyPositive,
    drsGte12,
    drsLt12,
    drsNegative,
    drsPositive,
    drsWeaklyPositive,
    icdscGte4,
    icdscLt4,
    icdscNegative,
    icdscPositive,
    icdscWeaklyPositive,
    nudescGte2,
    nudescLt2,
    nudescNegative,
    nudescPositive,
    nudescWeaklyPositive,
    tdcamNegative,
    tdcamPositive,
)
from digipod.criterion.patients import AdultPatients
from digipod.terminology.vocabulary import (
    ADMINISTRATION_OF_PROPHYLACTIC_DEXMEDETOMIDINE,
)

prophylacticDexmedetomidine = ProcedureOccurrence(
    static=False,
    concept=ADMINISTRATION_OF_PROPHYLACTIC_DEXMEDETOMIDINE,
    value=None,
)

# doesn't work because concept_ancestor table is empty and that table is required to infer drug concepts
# dexmedetomidineAdministered = DrugExposure(
#     ingredient_concept=Dexmedetomidine, dose=None, route=None,
# )

# workaround
class DexmedetomidineAdministration(Criterion):
    """
    Get Dexmedetomidine Administrations.

    Note: This is a workaround because currently concept_ancestor table is empty and that table is required to
    infer drug concepts.
    Actually this should be used:

    ```
    DrugExposure(
     ingredient_concept=Dexmedetomidine, dose=None, route=None,
     )
    ```
    """
    _static = False

    def __init__(self) -> None:
        super().__init__()
        self._set_omop_variables_from_domain("drug")

    def description(self) -> str:
        """
        Description of this criterion.
        """
        return "Dexmedetomidine Administration"

    def _create_query(self) -> Select:
        query = select(
            self._table.c.person_id,
            self._table.c.drug_exposure_start_datetime.label('interval_start'),
            self._table.c.drug_exposure_end_datetime.label('interval_end'),
            column_interval_type(IntervalType.POSITIVE),
        ).where(self._table.c.drug_concept_id == Dexmedetomidine.concept_id)

        query = self._filter_base_persons(query, c_person_id=self._table.c.person_id)
        query = self._filter_datetime(query)

        return query

dexmedetomidineAdministered = DexmedetomidineAdministration()

recommendation = Recommendation(
    expr=And(
        PopulationInterventionPairExpr(
            population_expr=And(
                AdultPatients(),
                Not(AnyTime(anyDementiaBeforeSurgery)),
                IntraOrPostOperative(dexmedetomidineAdministered),
                dexmedetomidineAdministered
            ),
            intervention_expr=And(
                AnyTime(prophylacticDexmedetomidine),
                Or(
                    Or(
                        BeforeFirstDexAdministration(nudescLt2),
                        BeforeFirstDexAdministration(nudescNegative),
                        BeforeFirstDexAdministration(nudescWeaklyPositive),
                        BeforeFirstDexAdministration(icdscLt4),
                        BeforeFirstDexAdministration(icdscNegative),
                        BeforeFirstDexAdministration(icdscWeaklyPositive),
                        BeforeFirstDexAdministration(camNegative),
                        BeforeFirstDexAdministration(drsLt12),
                        BeforeFirstDexAdministration(drsNegative),
                        BeforeFirstDexAdministration(drsWeaklyPositive),
                        BeforeFirstDexAdministration(dosLt3),
                        BeforeFirstDexAdministration(dosNegative),
                        BeforeFirstDexAdministration(dosWeaklyPositive),
                        BeforeFirstDexAdministration(tdcamNegative),
                        BeforeFirstDexAdministration(camicuNegative),
                        BeforeFirstDexAdministration(ddsLt8),
                        BeforeFirstDexAdministration(ddsNegative),
                        BeforeFirstDexAdministration(ddsWeaklyPositive),
                        BeforeFirstDexAdministration(FourAtLt4),
                        BeforeFirstDexAdministration(FourAtNegative),
                        BeforeFirstDexAdministration(FourAtWeaklyPositive),
                    ),
                    Or(
                        Not(BeforeFirstDexAdministration(nudescGte2)),
                        Not(BeforeFirstDexAdministration(nudescPositive)),
                        Not(BeforeFirstDexAdministration(icdscGte4)),
                        Not(BeforeFirstDexAdministration(icdscPositive)),
                        Not(BeforeFirstDexAdministration(camPositive)),
                        Not(BeforeFirstDexAdministration(drsGte12)),
                        Not(BeforeFirstDexAdministration(drsPositive)),
                        Not(BeforeFirstDexAdministration(dosGte3)),
                        Not(BeforeFirstDexAdministration(dosPositive)),
                        Not(BeforeFirstDexAdministration(tdcamPositive)),
                        Not(BeforeFirstDexAdministration(camicuPositive)),
                        Not(BeforeFirstDexAdministration(ddsGte7)),
                        Not(BeforeFirstDexAdministration(ddsPositive)),
                        Not(BeforeFirstDexAdministration(FourAtGte4)),
                        Not(BeforeFirstDexAdministration(FourAtPositive)),
                    ),
                )
            ),
            name="RecPlanSelectProphylacticDexAdministrationInPatsWithoutDementia",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanSelectProphylacticDexAdministrationInPatsWithoutDementia",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
        PopulationInterventionPairExpr(
            population_expr=NonSimplifiableAnd(AdultPatients(), anyDementiaBeforeSurgery),
            intervention_expr=IntraOrPostOperative(dexmedetomidineAdministered),
            name="RecPlanSelectProphylacticDexAdministrationInPatsWithDementia",
            url="https://fhir.charite.de/digipod/PlanDefinition/RecPlanSelectProphylacticDexAdministrationInPatsWithDementia",
            base_criterion=PatientsActiveDuringPeriod(),
        ),
    ),
    base_criterion=PatientsActiveDuringPeriod(),
    name="RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE",
    title="Recommendation Collection: Select 'prophylactic' if you administer dexmedetomidine intra- or postoperatively with the aim to prevent postoperative delirium after having balanced benefits and side effects in 'General Adult Surgical Patients With Dementia Preoperatively' or 'General Adult Surgical Patients Without Dementia Preoperatively nor Delirium Before Dexmedetomidine Administration'",
    url="https://fhir.charite.de/digipod/PlanDefinition/RecCollProphylacticDexAdministrationAfterBalancingBenefitsVSSE",
    version="0.4.0",
    description="Recommendation collection for adult patients getting dexmedetomidine during or after a surgical intervention of any type and independently of the type of anesthesia with the aim to prevent postoperative delirium (POD): Select 'prophylactic' if you administer dexmedetomidine with the aim to prevent postoperative delirium after having balanced benefits and side effects.",
    package_version="latest",
)
