import logging
from typing import Self

from execution_engine.converter.action.drug_administration import (
    DrugAdministrationAction,
)
from execution_engine.fhir import RecommendationPlan
from execution_engine.fhir.util import get_coding
from execution_engine.omop.criterion.noop import NoopCriterion
from execution_engine.omop.vocabulary import SNOMEDCT
from execution_engine.util import logic as logic

from digipod.concepts import SCT_SUBSTANCE


class NoopDrugAdministration(DrugAdministrationAction):
    """
    A drug administration action that does nothing. This is used when the drug
    administration uses the code for "substance", i.e. doesn't define any actual drug.
    """

    def __init__(self, exclude: bool):
        super(DrugAdministrationAction, self).__init__(exclude=exclude)

    @classmethod
    def from_fhir(cls, action_def: RecommendationPlan.Action) -> Self:
        """Creates a new action from a FHIR PlanDefinition."""

        if action_def.activity_definition_fhir is None:
            raise NotImplementedError("No activity defined for action")

        cc = action_def.activity_definition_fhir.productCodeableConcept
        coding = get_coding(cc)

        if SNOMEDCT.is_system(coding.system) and coding.code == SCT_SUBSTANCE:
            logging.warning(
                "Converting drug administration with SNOMED CT code 'Substance' to NoopCriterion"
            )

            exclude = (
                action_def.activity_definition_fhir.doNotPerform
                if action_def.activity_definition_fhir.doNotPerform is not None
                else False
            )

            return cls(exclude=exclude)
        else:
            return super().from_fhir(action_def)

    def _to_expression(self) -> logic.BaseExpr:
        return NoopCriterion()
