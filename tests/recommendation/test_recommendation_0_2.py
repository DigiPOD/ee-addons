import pytest

from digipod.recommendation.recommendation_0_2 import rec_0_2_Delirium_Screening
from digipod.tests.recommendation.resultset import ResultSet
from digipod.tests.recommendation.test_recommendation_base import TestRecommendationBase
from digipod.tests.recommendation.utils import AdultPatient


class TestRecommendation_0_2(TestRecommendationBase):

    recommendation = rec_0_2_Delirium_Screening

    @pytest.fixture
    def postop_icu_patient(self):
        pat = AdultPatient()
        pat.add_surgery(
            start="2024-12-01 09:00:00+01:00", end="2024-12-01 10:30:00+01:00"
        )
        pat.add_intensive_care_visit(
            start="2024-12-01 10:30:00+01:00", end="2024-12-06 12:00:00+01:00"
        )
        return pat

    def test_recommendation_0_2(self, postop_icu_patient):

        # postoperative patient ICU
        # until postoperative day 6, this patient should be screened for delirium in at least 2 shifts per day
        # icu scores are CAMICU, DDS and ICDSC

        pat = postop_icu_patient

        # 2 shifts CAM ICU screening
        pat.add_CAMICU(datetime="2024-12-01 11:00:00+01:00", score=0)
        pat.add_CAMICU(datetime="2024-12-01 18:00:00+01:00", score=0)

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [("2024-12-01 00:00:00+01:00", "2024-12-01 23:59:59+01:00", "POSITIVE")]
        )

        assert expected == result["POPULATION_INTERVENTION"]
