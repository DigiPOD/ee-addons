from typing import Any, Dict, Self

from execution_engine.constants import CohortCategory
from execution_engine.omop.criterion.abstract import Criterion
from sqlalchemy.sql import Select


class PreOperativeAdultBeforeDayOfSurgeryPatients(Criterion):
    """
    - >= 18 years
    - 42 days until end of day before surgery
    """

    def __init__(self) -> None:
        super().__init__(exclude=False, category=CohortCategory.POPULATION)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        """
        Create an object from a dictionary.
        """
        return cls(**data)

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return "PreOperativeAdultBeforeDayOfSurgeryPatients"

    def dict(self) -> dict:
        """
        Get a dictionary representation of the object.
        """
        return {
            "exclude": self._exclude,
            "category": self.category.value,
            "class": self.__class__.__name__,
        }

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """
        raise NotImplementedError()


class PreOperativePatientsBeforeEndOfSugergery(Criterion):
    """
    - >= 18 years
    - 42 days before day of surgery until end of surgery
    - vorstationär OR normalstationär
    """

    def __init__(self) -> None:
        super().__init__(exclude=False, category=CohortCategory.POPULATION)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        """
        Create an object from a dictionary.
        """
        return cls(**data)

    def description(self) -> str:
        """
        Get a description of the criterion.
        """
        return "PreOperativePatientsBeforeEndOfSugergery"

    def dict(self) -> dict:
        """
        Get a dictionary representation of the object.
        """
        return {
            "exclude": self._exclude,
            "category": self.category.value,
            "class": self.__class__.__name__,
        }

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """
        raise NotImplementedError()
