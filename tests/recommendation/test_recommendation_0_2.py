import pytest
from digipod.tests.recommendation.resultset import ResultSet
from digipod.tests.recommendation.test_recommendation_base import TestRecommendationBase
from digipod.tests.recommendation.utils import (
    DELIR_SCREENING_ICU_SCORES,
    DELIR_SCREENING_NORMALWARD_SCORES,
    AdultPatient,
)

from recommendation.recommendation_0_2 import rec_0_2_Delirium_Screening_double


class TestRecommendation_0_2(TestRecommendationBase):

    recommendation = rec_0_2_Delirium_Screening_double

    def postop_icu_patient(self):
        pat = AdultPatient()
        pat.add_surgery(
            start="2024-12-01 09:00:00+01:00", end="2024-12-01 10:30:00+01:00"
        )
        pat.add_intensive_care_visit(
            start="2024-12-01 10:30:00+01:00", end="2024-12-09 12:00:00+01:00"
        )
        return pat

    def postop_normalward_patient(self):
        pat = AdultPatient()
        pat.add_surgery(
            start="2024-12-01 09:00:00+01:00", end="2024-12-01 10:30:00+01:00"
        )
        pat.add_inpatient_visit(
            start="2024-12-01 10:30:00+01:00", end="2024-12-09 12:00:00+01:00"
        )
        return pat

    @staticmethod
    def add_score_assessments(pat, score, times):
        for time in times:
            pat.add_measurement(concept_id=score, datetime=time, value=0)

    @pytest.mark.parametrize("visit_type", ("icu", "normalward"))
    @pytest.mark.parametrize(
        "score",
        list(DELIR_SCREENING_ICU_SCORES.values())
        + list(DELIR_SCREENING_NORMALWARD_SCORES.values()),
        ids=list(DELIR_SCREENING_ICU_SCORES.keys())
        + list(DELIR_SCREENING_NORMALWARD_SCORES.keys()),
    )
    def test_single_assessment(self, score, visit_type):

        # postoperative patient ICU
        # until postoperative day 6, this patient should be screened for delirium in at least 2 shifts per day
        # icu scores are CAMICU, DDS and ICDSC

        if visit_type == "icu":
            pat = self.postop_icu_patient()
        else:
            pat = self.postop_normalward_patient()

        times = [
            # 1 shift screening (Morning)
            "2024-12-01 11:00:00+01:00",
            # 1 shift screening (Late)
            "2024-12-03 18:00:00+01:00",
            # 1 shift screening (night)
            "2024-12-06 23:00:00+01:00",
        ]

        self.add_score_assessments(pat, score, times)

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

    @pytest.mark.parametrize("visit_type", ("icu", "normalward"))
    @pytest.mark.parametrize(
        "score",
        list(DELIR_SCREENING_ICU_SCORES.values())
        + list(DELIR_SCREENING_NORMALWARD_SCORES.values()),
        ids=list(DELIR_SCREENING_ICU_SCORES.keys())
        + list(DELIR_SCREENING_NORMALWARD_SCORES.keys()),
    )
    def test_two_assessments(self, score, visit_type):

        # postoperative patient ICU
        # until postoperative day 6, this patient should be screened for delirium in at least 2 shifts per day
        # icu scores are CAMICU, DDS and ICDSC

        if visit_type == "icu":
            pat = self.postop_icu_patient()
        else:
            pat = self.postop_normalward_patient()

        times = [
            # 2 shifts screening (Morning, Late)
            "2024-12-01 11:00:00+01:00",
            "2024-12-01 18:00:00+01:00",
            # 2 shift screening (Morning, Night)
            "2024-12-03 11:00:00+01:00",
            "2024-12-03 23:00:00+01:00",
            # 2 shift screening (late, night)
            "2024-12-05 18:00:00+01:00",
            "2024-12-05 23:00:00+01:00",
            # 2 shift screening (night day before, morning)
            "2024-12-06 23:00:00+01:00",
            "2024-12-07 11:00:00+01:00",
        ]

        self.add_score_assessments(pat, score, times)

        self.commit_patient(pat)
        result = self.run_test()

        if (
            visit_type == "icu"
            and score in DELIR_SCREENING_ICU_SCORES.values()
            or visit_type == "normalward"
            and score in DELIR_SCREENING_NORMALWARD_SCORES.values()
        ):

            expected = ResultSet.from_tuples(
                [
                    (
                        "2024-12-01 10:30:00+01:00",
                        "2024-12-01 23:59:59+01:00",
                        "POSITIVE",
                    ),
                    (
                        "2024-12-02 00:00:00+01:00",
                        "2024-12-02 23:59:59+01:00",
                        "NEGATIVE",
                    ),
                    (
                        "2024-12-03 00:00:00+01:00",
                        "2024-12-03 23:59:59+01:00",
                        "POSITIVE",
                    ),
                    (
                        "2024-12-04 00:00:00+01:00",
                        "2024-12-04 23:59:59+01:00",
                        "NEGATIVE",
                    ),
                    (
                        "2024-12-05 00:00:00+01:00",
                        "2024-12-05 23:59:59+01:00",
                        "POSITIVE",
                    ),
                    (
                        "2024-12-06 00:00:00+01:00",
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
        else:
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

    @pytest.mark.parametrize("visit_type", ("icu", "normalward"))
    @pytest.mark.parametrize(
        "score",
        list(DELIR_SCREENING_ICU_SCORES.values())
        + list(DELIR_SCREENING_NORMALWARD_SCORES.values()),
        ids=list(DELIR_SCREENING_ICU_SCORES.keys())
        + list(DELIR_SCREENING_NORMALWARD_SCORES.keys()),
    )
    def test_three_assessments(self, score, visit_type):

        # postoperative patient ICU
        # until postoperative day 6, this patient should be screened for delirium in at least 2 shifts per day
        # icu scores are CAMICU, DDS and ICDSC

        if visit_type == "icu":
            pat = self.postop_icu_patient()
        else:
            pat = self.postop_normalward_patient()

        times = [
            # 3 shifts screening (Morning, Late, Night)
            "2024-12-01 11:00:00+01:00",
            "2024-12-01 18:00:00+01:00",
            "2024-12-01 23:00:00+01:00",
            # 3 shifts screening (Morning, Late, Night)
            "2024-12-03 11:00:00+01:00",
            "2024-12-03 18:00:00+01:00",
            "2024-12-03 23:00:00+01:00",
            # 3 shifts screening (Morning, Late, Night)
            "2024-12-05 11:00:00+01:00",
            "2024-12-05 18:00:00+01:00",
            "2024-12-05 23:00:00+01:00",
            # 3 shifts screening (Morning, Late, Night)
            "2024-12-06 11:00:00+01:00",
            "2024-12-07 18:00:00+01:00",
            "2024-12-07 23:00:00+01:00",
        ]

        self.add_score_assessments(pat, score, times)

        self.commit_patient(pat)
        result = self.run_test()

        if (
            visit_type == "icu"
            and score in DELIR_SCREENING_ICU_SCORES.values()
            or visit_type == "normalward"
            and score in DELIR_SCREENING_NORMALWARD_SCORES.values()
        ):

            expected = ResultSet.from_tuples(
                [
                    (
                        "2024-12-01 10:30:00+01:00",
                        "2024-12-01 23:59:59+01:00",
                        "POSITIVE",
                    ),
                    (
                        "2024-12-02 00:00:00+01:00",
                        "2024-12-02 23:59:59+01:00",
                        "NEGATIVE",
                    ),
                    (
                        "2024-12-03 00:00:00+01:00",
                        "2024-12-03 23:59:59+01:00",
                        "POSITIVE",
                    ),
                    (
                        "2024-12-04 00:00:00+01:00",
                        "2024-12-04 23:59:59+01:00",
                        "NEGATIVE",
                    ),
                    # positive from 5th - 7th, because the 3rd assessment on the 5th is counted both 1x for the 5th
                    # (22:00-00:00) and 1x for the 6th (00:00-06:00), because the whole duration of the shift is "positive"
                    (
                        "2024-12-05 00:00:00+01:00",
                        "2024-12-06 23:59:59+01:00",
                        "POSITIVE",
                    ),
                    (
                        "2024-12-07 00:00:00+01:00",
                        "2024-12-09 12:00:00+01:00",
                        "NOT_APPLICABLE",
                    ),  # 2024-12-06 = postoperative day 5
                ]
            )

        else:
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

    def test_two_assessments_different_scores(self):

        pat = self.postop_icu_patient()

        # 2 shifts screening (Morning, Late)
        pat.add_CAMICU("2024-12-01 11:00:00+01:00", score=0)
        pat.add_DDS("2024-12-01 18:00:00+01:00", score=0)

        # 2 shift screening (Morning, Night)
        pat.add_ICDSC("2024-12-03 11:00:00+01:00", score=0)
        pat.add_CAMICU("2024-12-03 23:00:00+01:00", score=0)

        # 2 shift screening (late, night)
        pat.add_DDS("2024-12-05 18:00:00+01:00", score=0)
        pat.add_ICDSC("2024-12-05 23:00:00+01:00", score=0)

        self.commit_patient(pat)
        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "POSITIVE",
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "POSITIVE",
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "POSITIVE",
                ),
                (
                    "2024-12-06 00:00:00+01:00",
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
