from datetime import datetime
from typing import Any

import pandas as pd
import pendulum


class ResultSet:
    def __init__(self, intervals):
        # Standardize all datetime objects to Python's datetime.datetime with timezone info
        self.intervals = sorted(
            [
                {
                    "interval_start": self._to_datetime_with_tz(i["interval_start"]),
                    "interval_end": self._to_datetime_with_tz(i["interval_end"]),
                    "interval_type": i["interval_type"],
                }
                for i in intervals
            ],
            key=lambda x: (x["interval_start"], x["interval_end"], x["interval_type"]),
        )

    @staticmethod
    def _to_datetime_with_tz(dt):
        """Ensure the datetime object has timezone information and is a Python datetime."""
        if isinstance(dt, pendulum.DateTime):
            return dt.in_tz("local").naive().astimezone()  # Ensure local timezone
        elif isinstance(dt, pd.Timestamp):
            return (
                dt.to_pydatetime().astimezone()
            )  # Convert pandas.Timestamp to datetime
        elif isinstance(dt, datetime):
            return dt.astimezone()  # Ensure it has timezone info
        elif isinstance(dt, str):
            return pendulum.parse(
                dt
            ).astimezone()  # Parse strings as pendulum, then convert
        else:
            raise ValueError(f"Unsupported datetime type: {type(dt)}")

    @classmethod
    def from_dataframe(cls, df):
        """Create a ResultSet from a pandas DataFrame."""
        intervals = [
            {
                "interval_start": row["interval_start"],
                "interval_end": row["interval_end"],
                "interval_type": row["interval_type"],
            }
            for _, row in df.iterrows()
        ]
        return cls(intervals)

    @classmethod
    def from_tuples(cls, tuples):
        """Create a ResultSet from a list of tuples."""
        intervals = [
            {
                "interval_start": t[0],
                "interval_end": t[1],
                "interval_type": t[2],
            }
            for t in tuples
        ]
        return cls(intervals)

    def pretty_print(self):
        """Pretty print the contents of the ResultSet as a table with vertical separators and local timezone formatting."""
        headers = ["Interval Start", "Interval End", "Interval Type"]
        col_widths = [25, 25, 20]

        header_row = f"{headers[0]:<{col_widths[0]}} | {headers[1]:<{col_widths[1]}} | {headers[2]:<{col_widths[2]}}"
        print(header_row)
        print("-" * (sum(col_widths) + 6))

        for interval in self.intervals:
            row = (
                f"{interval['interval_start'].isoformat():<{col_widths[0]}} | "
                f"{interval['interval_end'].isoformat():<{col_widths[1]}} | "
                f"{interval['interval_type']:<{col_widths[2]}}"
            )
            print(row)

    def comparison_report(self, other: Any) -> list[str]:
        """Generate a detailed comparison report for pytest_assertrepr_compare."""
        if not isinstance(other, ResultSet):
            return ["Comparison is not valid: other object is not a ResultSet."]

        report = ["Comparison report:"]
        self_set = set(map(tuple, [dict(sorted(d.items())) for d in self.intervals]))
        other_set = set(map(tuple, [dict(sorted(d.items())) for d in other.intervals]))

        missing_in_other = self_set - other_set
        extra_in_other = other_set - self_set

        if missing_in_other:
            report.append("Missing in other:")
            for item in sorted(missing_in_other):
                report.append(f"  {item}")

        if extra_in_other:
            report.append("Extra in other:")
            for item in sorted(extra_in_other):
                report.append(f"  {item}")

        if not missing_in_other and not extra_in_other:
            report.append("No differences found.")

        return report

    def __repr__(self):
        return f"ResultSet({self.intervals})"
