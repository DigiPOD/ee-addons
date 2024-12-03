import pytest

from digipod.tests.recommendation.test_recommendation_base import TestRecommendationBase
from digipod.tests.recommendation.utils import AdultPatient


class TestRecommendation_0_2(TestRecommendationBase):

    @pytest.fixture
    def adult_patient_with_surgery(self):
        pat = AdultPatient()
        pat.add_surgery(start="2024-12-01 09:00:00", end="2024-12-01 10:30:00")
        return pat

    def test_recommendation_0_2(self, adult_patient_with_surgery):
        self.commit_patient(adult_patient_with_surgery)
