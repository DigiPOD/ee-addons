
import pandas as pd
import pytest
from execution_engine.constants import CohortCategory
from execution_engine.omop import cohort
from execution_engine.omop.db.celida.views import interval_result
from execution_engine.util.types.timerange import TimeRange
from sqlalchemy import select

from digipod.tests.recommendation.resultset import ResultSet


class TestRecommendationBase:

    observation_window = TimeRange(
        start="2024-11-29 08:00:00+01:00",
        end="2024-12-15 08:00:00+01:00",
    )
    run_id: int | None = None
    recommendation: cohort.Recommendation | None = None

    @pytest.fixture(autouse=True)
    def _setup(self, db_session):
        self.db = db_session

    def setup_method(self, method):
        from execution_engine.execution_engine import ExecutionEngine

        assert self.recommendation is not None, "Set recommendation first"

        e = ExecutionEngine(verbose=False)

        e.register_recommendation(self.recommendation)

    def teardown_method(self, method):
       self.recommendation.reset_state()

    def commit_patient(self, pat):

        person = pat.person
        person.person_id = None  # reset person id
        self.db.add(person)
        self.db.commit()

        for obj in pat.yield_objects():
            obj.person_id = person.person_id
            self.db.add(obj)

        self.db.commit()

    def fetch_interval_result(
        self,
        db_session,
        pi_pair_id: int | None,
        criterion_id: int | None,
        category: CohortCategory | None,
    ) -> pd.DataFrame:
        return self._fetch_result_view(
            interval_result, db_session, pi_pair_id, criterion_id, category
        )

    def _fetch_result_view(
        self,
        view,
        db_session,
        pi_pair_id: int | None,
        criterion_id: int | None,
        category: CohortCategory | None,
    ) -> dict[str, pd.DataFrame]:
        assert self.run_id is not None, "Run test first"
        stmt = select(view).where(view.c.run_id == self.run_id)

        if criterion_id is not None:
            stmt = stmt.where(view.c.criterion_id == criterion_id)
        else:
            stmt = stmt.where(view.c.criterion_id.is_(None))

        if pi_pair_id is not None:
            stmt = stmt.where(view.c.pi_pair_id == pi_pair_id)
        else:
            stmt = stmt.where(view.c.pi_pair_id.is_(None))

        if category is not None:
            stmt = stmt.where(view.c.cohort_category == category)

        df = pd.read_sql(
            stmt,
            db_session.bind,
            params={"run_id": self.run_id},
        )

        return df

    def run_test(self) -> pd.DataFrame:
        from execution_engine.clients import omopdb
        from execution_engine.execution_engine import ExecutionEngine

        assert self.recommendation is not None, "Set recommendation first"

        e = ExecutionEngine(verbose=False)

        self.run_id = e.execute(
            self.recommendation,
            start_datetime=self.observation_window.start,
            end_datetime=self.observation_window.end,
        )

        df = self.fetch_interval_result(
            omopdb.session(), pi_pair_id=None, criterion_id=None, category=None
        )

        return {
            cohort: ResultSet.from_dataframe(
                df.query("cohort_category==@cohort").sort_values(
                    by=["person_id", "interval_start"]
                )[["person_id", "interval_start", "interval_end", "interval_type", "interval_ratio"]]
            )
            for cohort in CohortCategory
        }
