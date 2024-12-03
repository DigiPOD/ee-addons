import pytest

from digipod.tests.recommendation.utils import Patient


class TestRecommendationBase:

    @pytest.fixture(autouse=True)
    def _setup(self, db_session):
        self.db = db_session

    def commit_patient(self, pat: Patient):

        person = pat.person
        person.person_id = None  # reset person id
        self.db.add(person)
        self.db.commit()

        for obj in pat.yield_objects():
            obj.person_id = person.person_id
            self.db.add(obj)

        self.db.commit()
