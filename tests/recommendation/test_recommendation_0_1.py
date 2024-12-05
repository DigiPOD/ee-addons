import pytest

from digipod.recommendation.recommendation_0_1 import rec_0_1_Delirium_Screening
from digipod.tests.recommendation.resultset import ResultSet
from digipod.tests.recommendation.test_recommendation_base import TestRecommendationBase
from digipod.tests.recommendation.utils import (
    DELIR_SCREENING_NORMALWARD_SCORES,
    AdultPatient,
)


class TestRecommendation_0_1(TestRecommendationBase):

    recommendation = rec_0_1_Delirium_Screening

    def preop_inpatient(self):
        pat = AdultPatient()
        pat.add_surgery(
            start="2024-12-10 09:00:00+01:00", end="2024-12-10 10:30:00+01:00"
        )
        pat.add_inpatient_visit(
            start="2024-12-01 10:30:00+01:00", end="2024-12-30 12:00:00+01:00"
        )
        return pat

    def preop_outpatient(self):
        pat = AdultPatient()
        pat.add_surgery(
            start="2024-12-10 09:00:00+01:00", end="2024-12-10 10:30:00+01:00"
        )
        pat.add_outpatient_visit(
            start="2024-12-01 10:30:00+01:00", end="2024-12-30 12:00:00+01:00"
        )
        return pat

    @staticmethod
    def add_score_assessments(pat, score, times):
        for time in times:
            pat.add_measurement(concept_id=score, datetime=time, value=0)

    @pytest.mark.parametrize("visit_type", ("inpatient", "outpatient"))
    @pytest.mark.parametrize(
        "score",
        list(DELIR_SCREENING_NORMALWARD_SCORES.values()),
        ids=list(DELIR_SCREENING_NORMALWARD_SCORES.keys()),
    )
    @pytest.mark.parametrize(
        "timepoint", ["2024-12-01 11:00:00+01:00", "2024-12-10 08:59:00+01:00"]
    )
    def test_single_assessment(self, score, visit_type, timepoint):

        # postoperative patient ICU
        # until postoperative day 6, this patient should be screened for delirium in at least 2 shifts per day
        # icu scores are CAMICU, DDS and ICDSC

        if visit_type == "inpatient":
            pat = self.preop_inpatient()
        else:
            pat = self.preop_outpatient()

        pat.add_measurement(concept_id=score, datetime=timepoint, value=0)

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",  # start of visit
                    "2024-12-10 10:30:00+01:00",  # end of procedure
                    "POSITIVE",
                ),
                (
                    "2024-12-10 10:30:01+01:00",  # end of procedure + 1 sec
                    "2024-12-15 08:00:00+01:00",  # end of observation window
                    "NOT_APPLICABLE",
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]
