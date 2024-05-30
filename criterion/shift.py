from execution_engine.omop.criterion.abstract import Criterion
from sqlalchemy.sql import Select


class Shift(Criterion):
    """
    - >= 18 years
    - 42 days until end of day before surgery
    """

    shift_start: int
    shift_end: int

    def _create_query(self) -> Select:
        """
        Get the SQL Select query for data required by this criterion.
        """
        raise NotImplementedError()

        # SELECT
        #     generate_series(start_date::timestamp, end_date::timestamp, '1 day') AS start_datetime,
        #     generate_series(start_date::timestamp, end_date::timestamp, '1 day') + INTERVAL '8 hours' AS actual_start,
        #     generate_series(start_date::timestamp, end_date::timestamp, '1 day') + INTERVAL '16 hours' AS end_datetime
        # FROM
        #     (SELECT '2023-01-01'::date AS start_date, '2023-01-07'::date AS end_date) AS date_range;

        # rather:
        # WITH daily_measurements AS (
        #     SELECT
        #         DATE(measurement_datetime) AS measurement_date,
        #         MIN(measurement_datetime) AS start_datetime,
        #         MAX(measurement_datetime) AS end_datetime,
        #         BOOL_OR(value_as_number > threshold) AS above_threshold  -- Change to < for below threshold
        #     FROM
        #         measurement
        #     WHERE
        #         EXTRACT(HOUR FROM measurement_datetime AT TIME ZONE 'UTC') >= 8 AND  -- Adjust time zone if necessary
        #         EXTRACT(HOUR FROM measurement_datetime AT TIME ZONE 'UTC') < 16
        #     GROUP BY
        #         DATE(measurement_datetime)
        # )
        #
        # SELECT
        #     start_datetime,
        #     end_datetime + INTERVAL '1 day' - INTERVAL '1 second' AS end_datetime,  -- To make it end of day
        #     NOT above_threshold AS valid  -- Change logic here if "valid" means below the threshold
        # FROM
        #     daily_measurements;


class MorningShift(Shift):
    """
    Morning shift from 8 am to 4 pm
    """

    shift_start = 8
    shift_end = 16


class AfternoonShift(Shift):
    """
    Afternoon shift from 16 pm to 24 pm

    """

    shift_start = 16
    shift_end = 24


class NightShift(Shift):
    """
    Night shift from 24 pm to 8 am
    """

    shift_start = 24
    shift_end = 8
