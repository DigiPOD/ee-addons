
from digipod.tests.recommendation.resultset import ResultSet
from digipod.tests.recommendation.test_recommendation_base import TestRecommendationBase


class TestRecommendation_4_3(TestRecommendationBase):

    def setup_method(self, method):
        from digipod.recommendation import recommendation_4_3
        self.recommendation = recommendation_4_3.recommendation
        super(TestRecommendation_4_3, self).setup_method(method)


    def postop_icu_patient(self):
        from digipod.tests.recommendation.utils import (
            ElderlyPatient,
        )
        pat = ElderlyPatient()
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

    @staticmethod
    def add_procedure(pat, procedure, time):
        pat.add_procedure(concept_id=procedure.concept_id, datetime=time)

    def test_anxiety(self):
        """
        Faces Anxiety Scale should be assessed 1x per day.
        If it is assessed, the bundle is at 100%, meaning the whole recommendation is at 25% - otherwise 0%.
        """
        from digipod.terminology.custom_concepts import FACES_ANXIETY_SCALE_SCORE

        pat = self.postop_icu_patient()

        times = [
            "2024-12-01 11:00:00+01:00",
            "2024-12-02 11:00:00+01:00",
            "2024-12-04 11:00:00+01:00",
            "2024-12-06 11:00:00+01:00",
            "2024-12-07 11:00:00+01:00", # > 5d postop - shouldn't be counted
        ]

        self.add_score_assessments(pat, FACES_ANXIETY_SCALE_SCORE.concept_id, times)

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_cognition(self):
        """
        One of the four cognition items should be performed each day.
        If any one is performed, this bundle is at 100% and the whole recommendation at 25% - otherwise 0%.
        """
        from digipod.criterion.non_pharma_measures import (
            COGNITIVE_STIMULATION,
            COMMUNICATION_AID_PROVISION,
            REALITY_ORIENTATION,
        )
        from digipod.terminology.custom_concepts import (
            NON_PHARMACOLOGICAL_INTERVENTION_TO_SUPPORT_THE_CIRCADIAN_RHYTHM,
        )


        pat = self.postop_icu_patient()

        self.add_procedure(pat, NON_PHARMACOLOGICAL_INTERVENTION_TO_SUPPORT_THE_CIRCADIAN_RHYTHM, "2024-12-02 11:00:00+01:00")

        self.add_procedure(pat, REALITY_ORIENTATION,
                           "2024-12-03 11:00:00+01:00")
        self.add_procedure(pat, COMMUNICATION_AID_PROVISION,
                           "2024-12-04 11:00:00+01:00")

        self.add_procedure(pat, COGNITIVE_STIMULATION,
                           "2024-12-06 11:00:00+01:00")

        # > 5d postop - shouldn't be counted
        self.add_procedure(pat, NON_PHARMACOLOGICAL_INTERVENTION_TO_SUPPORT_THE_CIRCADIAN_RHYTHM, "2024-12-07 11:00:00+01:00")


        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_mobilization(self):
        """
        If ability to mobilize is assessed and the value is
            - anything but DOES_NOT_MOBILIZE -> 100%
            - DOES_NOT_MOBILIZE:
                - if patient is mobilized -> 100%
                - if patient is not mobilized -> %50

        otherwise 0%.

        Whole recommendation = values / 4.

        """
        from digipod.criterion.non_pharma_measures import (
            ABILITY_TO_MOBILIZE,
            DOES_NOT_MOBILIZE,
            PHYSIATRIC_JOINT_MOBILIZATION,
        )

        pat = self.postop_icu_patient()

        # day 2: able to self mobilize -> 100% bundle, 25% total
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, "2024-12-02 11:00:00+01:00")

        # day 4: not able to self mobilize and no mobilization -> 50% bundle, 12.5% total
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, "2024-12-04 11:00:00+01:00", value_as_concept=DOES_NOT_MOBILIZE.concept_id)

        # day 6: not able to self mobilize and mobilization -> 100% bundle, 25% total
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, "2024-12-06 11:00:00+01:00",
                            value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_procedure(PHYSIATRIC_JOINT_MOBILIZATION.concept_id, datetime="2024-12-06 11:00:00+01:00")

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.125
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_feeding_self_feeding(self):
        """
        At least one of the following 3 must be fulfilled for 100% (i.e. we should take max(interval_ratio) over these):
        - Self feeding
            - not evaluated -> 0%
            - evaluated
                - enteral feeding -> 100%
                - no enteral feeding -> 50%

        - Deglutition
            - not evaluated -> 0%
            - evaluated
              - dysphagia therapy OR nutritional regime modification -> 100%
              - no therapy / modification -> 50%

        - Mouth Care
            - not performed -> 0%
            - performed -> 100%
        """

        from digipod.criterion.non_pharma_measures import (
            ABILITY_TO_FEED_SELF,
            DOES_NOT_FEED_SELF,
            ENTERAL_FEEDING,
        )

        pat = self.postop_icu_patient()

        # day 2: able to feed self -> 100% bundle, 25% total
        pat.add_observation(ABILITY_TO_FEED_SELF.concept_id, "2024-12-02 11:00:00+01:00")

        # day 4: not able to feed self and no enteral feeding -> 50% bundle, 12.5% total
        pat.add_observation(ABILITY_TO_FEED_SELF.concept_id, "2024-12-04 11:00:00+01:00",
                            value_as_concept=DOES_NOT_FEED_SELF.concept_id)

        # day 6: not able to feed self and enteral feeding -> 100% bundle, 25% total
        pat.add_observation(ABILITY_TO_FEED_SELF.concept_id, "2024-12-06 11:00:00+01:00",
                            value_as_concept=DOES_NOT_FEED_SELF.concept_id)
        pat.add_procedure(ENTERAL_FEEDING.concept_id, datetime="2024-12-06 11:00:00+01:00")

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.125
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_feeding_deglutition(self):
        """
        At least one of the following 3 must be fulfilled for 100% (i.e. we should take max(interval_ratio) over these):
        - Self feeding
            - not evaluated -> 0%
            - evaluated
                - enteral feeding -> 100%
                - no enteral feeding -> 50%

        - Deglutition
            - not evaluated -> 0%
            - evaluated
              - dysphagia therapy OR nutritional regime modification -> 100%
              - no therapy / modification -> 50%

        - Mouth Care
            - not performed -> 0%
            - performed -> 100%
        """

        from digipod.criterion.non_pharma_measures import (
            DEGLUTITION,
            DIFFICULTY_SWALLOWING,
            DYSPHAGIA_THERAPY,
            NUTRITIONAL_REGIME_MODIFICATION,
        )

        pat = self.postop_icu_patient()

        # day 2: able to swallow -> 100% bundle, 25% total
        pat.add_observation(DEGLUTITION.concept_id, "2024-12-02 11:00:00+01:00")

        # day 3: not able to swallow and no therapy-> 50% bundle, 12.5% total
        pat.add_observation(DEGLUTITION.concept_id, "2024-12-03 11:00:00+01:00",
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)

        # day 4: not able to swallow and dysphagia therapy-> 100% bundle, 25% total
        pat.add_observation(DEGLUTITION.concept_id, "2024-12-04 11:00:00+01:00",
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)
        pat.add_procedure(DYSPHAGIA_THERAPY.concept_id, datetime="2024-12-04 11:00:00+01:00")

        # day 6: not able to swallow and nutritional regime change -> 100% bundle, 25% total
        pat.add_observation(DEGLUTITION.concept_id, "2024-12-06 11:00:00+01:00",
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)
        pat.add_procedure(NUTRITIONAL_REGIME_MODIFICATION.concept_id, datetime="2024-12-06 11:00:00+01:00")

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "NEGATIVE",
                    0.125
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_feeding_mouth_care(self):
        """
        At least one of the following 3 must be fulfilled for 100% (i.e. we should take max(interval_ratio) over these):
        - Self feeding
            - not evaluated -> 0%
            - evaluated
                - enteral feeding -> 100%
                - no enteral feeding -> 50%

        - Deglutition
            - not evaluated -> 0%
            - evaluated
              - dysphagia therapy OR nutritional regime modification -> 100%
              - no therapy / modification -> 50%

        - Mouth Care
            - not performed -> 0%
            - performed -> 100%
        """

        from digipod.criterion.non_pharma_measures import MOUTH_CARE_MANAGEMENT

        pat = self.postop_icu_patient()

        # day 3,4,6: mouth care -> 100% bundle, 25% total
        pat.add_procedure(MOUTH_CARE_MANAGEMENT.concept_id, "2024-12-03 11:00:00+01:00")
        pat.add_procedure(MOUTH_CARE_MANAGEMENT.concept_id, "2024-12-04 11:00:00+01:00")
        pat.add_procedure(MOUTH_CARE_MANAGEMENT.concept_id, "2024-12-06 11:00:00+01:00")

        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-06 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-07 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]


    def test_combination_1(self):
        """
        Test combination of criteria
        """
        from digipod.criterion.non_pharma_measures import (
            ABILITY_TO_FEED_SELF,
            ABILITY_TO_MOBILIZE,
            COGNITIVE_STIMULATION,
            COMMUNICATION_AID_PROVISION,
            REALITY_ORIENTATION,
        )
        from digipod.terminology.custom_concepts import (
            FACES_ANXIETY_SCALE_SCORE,
            NON_PHARMACOLOGICAL_INTERVENTION_TO_SUPPORT_THE_CIRCADIAN_RHYTHM,
        )

        pat = self.postop_icu_patient()

        # day 2
        dt = "2024-12-02 11:00:00+01:00"
        pat.add_procedure(REALITY_ORIENTATION.concept_id, dt)

        # day 3
        dt = "2024-12-03 11:00:00+01:00"
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, dt, value=0)
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, dt)

        # day 4
        dt = "2024-12-04 11:00:00+01:00"
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, dt, value=0)
        pat.add_procedure(COGNITIVE_STIMULATION.concept_id, dt)
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, dt)

        # day 5
        dt = "2024-12-05 11:00:00+01:00"
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, dt, value=0)
        pat.add_procedure(NON_PHARMACOLOGICAL_INTERVENTION_TO_SUPPORT_THE_CIRCADIAN_RHYTHM.concept_id, dt)
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, dt)
        pat.add_observation(ABILITY_TO_FEED_SELF.concept_id, dt)


        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "NEGATIVE",
                    0.5
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.75
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "POSITIVE",
                    1.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_combination_2(self):
        """
        Test combination of criteria
        """
        from digipod.criterion.non_pharma_measures import (
            ABILITY_TO_FEED_SELF,
            ABILITY_TO_MOBILIZE,
            COMMUNICATION_AID_PROVISION,
            DOES_NOT_FEED_SELF,
            DOES_NOT_MOBILIZE,
            ENTERAL_FEEDING,
            PHYSIATRIC_JOINT_MOBILIZATION,
        )
        from digipod.terminology.custom_concepts import FACES_ANXIETY_SCALE_SCORE


        pat = self.postop_icu_patient()

        # day 2 - 25%
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, "2024-12-02 11:00:00+01:00", value=0)

        # day 3 - (2x100% + 50%) / 4 = 62.5%
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, "2024-12-03 11:00:00+01:00", value=0)
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, "2024-12-03 11:00:00+01:00")
        # only 50%
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, "2024-12-03 11:00:00+01:00", value_as_concept=DOES_NOT_MOBILIZE.concept_id)



        # day 4 - (3x100% + 50%) / 4 = 87.5%
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, "2024-12-04 11:00:00+01:00", value=0)
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, "2024-12-04 11:00:00+01:00")
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, "2024-12-04 11:00:00+01:00",
                            value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_procedure(PHYSIATRIC_JOINT_MOBILIZATION.concept_id, datetime="2024-12-04 11:00:00+01:00")
        # only 50%
        pat.add_observation(ABILITY_TO_FEED_SELF.concept_id, "2024-12-04 11:00:00+01:00",
                            value_as_concept=DOES_NOT_FEED_SELF.concept_id)

        # day 5 - 4x100% / 4 = 100%
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, "2024-12-05 11:00:00+01:00", value=0)
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, "2024-12-05 11:00:00+01:00")
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, "2024-12-05 11:00:00+01:00",
                            value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_procedure(PHYSIATRIC_JOINT_MOBILIZATION.concept_id, datetime="2024-12-05 11:00:00+01:00")
        pat.add_observation(ABILITY_TO_FEED_SELF.concept_id, "2024-12-05 11:00:00+01:00",
                            value_as_concept=DOES_NOT_FEED_SELF.concept_id)
        pat.add_procedure(ENTERAL_FEEDING.concept_id, datetime="2024-12-05 11:00:00+01:00")


        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-03 23:59:59+01:00",
                    "NEGATIVE",
                    0.625
                ),
                (
                    "2024-12-04 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.875
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "POSITIVE",
                    1.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]

    def test_combination_3(self):
        """
        Test combination of criteria
        """
        from digipod.criterion.non_pharma_measures import (
            ABILITY_TO_MOBILIZE,
            COMMUNICATION_AID_PROVISION,
            DEGLUTITION,
            DIFFICULTY_SWALLOWING,
            DOES_NOT_MOBILIZE,
            DYSPHAGIA_THERAPY,
            NUTRITIONAL_REGIME_MODIFICATION,
            PHYSIATRIC_JOINT_MOBILIZATION,
        )
        from digipod.terminology.custom_concepts import FACES_ANXIETY_SCALE_SCORE

        pat = self.postop_icu_patient()

        # day 2 - 2x50% / 4 = 25%
        dt = "2024-12-02 11:00:00+01:00"
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, dt, value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_observation(DEGLUTITION.concept_id, dt,
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)

        # day 3 - (2x100% + 2x50%) / 4 = 75%
        dt = "2024-12-03 11:00:00+01:00"
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, dt, value=0)
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, dt)
        # only 50%
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, dt, value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_observation(DEGLUTITION.concept_id, dt,
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)

        # day 4 - (3x100%) / 4 = 75%
        dt = "2024-12-04 11:00:00+01:00"
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, dt)
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, dt,
                            value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_procedure(PHYSIATRIC_JOINT_MOBILIZATION.concept_id, datetime=dt)
        pat.add_observation(DEGLUTITION.concept_id, dt,
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)
        pat.add_procedure(NUTRITIONAL_REGIME_MODIFICATION.concept_id, datetime=dt)

        # day 5 - 4x100% / 4 = 100%
        dt = "2024-12-05 11:00:00+01:00"
        pat.add_measurement(FACES_ANXIETY_SCALE_SCORE.concept_id, dt, value=0)
        pat.add_procedure(COMMUNICATION_AID_PROVISION.concept_id, dt)
        pat.add_observation(ABILITY_TO_MOBILIZE.concept_id, dt,
                            value_as_concept=DOES_NOT_MOBILIZE.concept_id)
        pat.add_procedure(PHYSIATRIC_JOINT_MOBILIZATION.concept_id, datetime=dt)
        pat.add_observation(DEGLUTITION.concept_id, dt,
                            value_as_concept=DIFFICULTY_SWALLOWING.concept_id)
        pat.add_procedure(DYSPHAGIA_THERAPY.concept_id, datetime=dt)


        self.commit_patient(pat)

        result = self.run_test()

        expected = ResultSet.from_tuples(
            [
                (
                    "2024-12-01 10:30:00+01:00",
                    "2024-12-01 23:59:59+01:00",
                    "NEGATIVE",
                    0.0
                ),
                (
                    "2024-12-02 00:00:00+01:00",
                    "2024-12-02 23:59:59+01:00",
                    "NEGATIVE",
                    0.25
                ),
                (
                    "2024-12-03 00:00:00+01:00",
                    "2024-12-04 23:59:59+01:00",
                    "NEGATIVE",
                    0.75
                ),
                (
                    "2024-12-05 00:00:00+01:00",
                    "2024-12-05 23:59:59+01:00",
                    "POSITIVE",
                    1.0
                ),
                (
                    "2024-12-06 00:00:00+01:00",
                    "2024-12-09 12:00:00+01:00",
                    "NEGATIVE",
                    0.0
                ),
            ]
        )

        assert expected == result["POPULATION_INTERVENTION"]
