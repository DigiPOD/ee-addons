
from digipod.terminology.custom_concepts import FACES_ANXIETY_SCALE_SCORE
from digipod.tests.recommendation.resultset import ResultSet
from digipod.tests.recommendation.test_recommendation_base import TestRecommendationBase
from digipod.tests.recommendation.utils import (
    AdultPatient,
)


class TestRecommendation_4_3(TestRecommendationBase):

    def postop_icu_patient(self):
        pat = AdultPatient()
        pat.add_surgery(
            start="2024-12-01 09:00:00+01:00", end="2024-12-01 10:30:00+01:00"
        )
        pat.add_intensive_care_visit(
            start="2024-12-01 10:30:00+01:00", end="2024-12-09 12:00:00+01:00"
        )
        return pat


    @staticmethod
    def add_score_assessments(pat, score, times):
        for time in times:
            pat.add_measurement(concept_id=score, datetime=time, value=0)

    # @pytest.mark.parametrize("visit_type", ("icu", "normalward"))
    # @pytest.mark.parametrize(
    #     "score",
    #     list(DELIR_SCREENING_ICU_SCORES.values())
    #     + list(DELIR_SCREENING_NORMALWARD_SCORES.values()),
    #     ids=list(DELIR_SCREENING_ICU_SCORES.keys())
    #     + list(DELIR_SCREENING_NORMALWARD_SCORES.keys()),
    # )
    def text_anxiety(self):
        pat = self.postop_icu_patient()

        times = [
            "2024-12-01 11:00:00+01:00",
            "2024-12-02 11:00:00+01:00",
            "2024-12-04 11:00:00+01:00",
            "2024-12-06 11:00:00+01:00",
            "2024-12-07 11:00:00+01:00",
        ]

        self.add_score_assessments(pat, FACES_ANXIETY_SCALE_SCORE, times)

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                ),  # 2024-12-06 = postoperative day 5
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NOT_APPLICABLE",
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]
