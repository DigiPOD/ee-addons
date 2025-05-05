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
                    "interval_ratio": i["interval_ratio"],
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
        elif isinstance(dt, int):
            return datetime.fromtimestamp(dt).astimezone()
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
                "interval_ratio": row["interval_ratio"],
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
                "interval_ratio": t[3],
            }
            for t in tuples
        ]
        return cls(intervals)

    def pretty_print(self):
        """Pretty print the contents of the ResultSet as a table with vertical separators and local timezone formatting."""
        headers = ["Interval Start", "Interval End", "Type", "Ratio"]
        col_widths = [25, 25, 14, 6]

        header_row = f"{headers[0]:<{col_widths[0]}} | {headers[1]:<{col_widths[1]}} | {headers[2]:<{col_widths[2]}} | {headers[3]:<{col_widths[3]}}"
        print(header_row)
        print("-" * (sum(col_widths) + 8))

        for interval in self.intervals:
            ratio = interval["interval_ratio"]
            ratio_display = f"{ratio:.2f}" if ratio is not None else "-"
            row = (
                f"{interval['interval_start'].isoformat():<{col_widths[0]}} | "
                f"{interval['interval_end'].isoformat():<{col_widths[1]}} | "
                f"{interval['interval_type']:<{col_widths[2]}} | "
                f"{ratio_display:<{col_widths[3]}}"
            )
            print(row)

    def __eq__(self, other: Any) -> bool:
        """Check if two ResultSet objects are equal, ignoring the order of intervals."""
        if not isinstance(other, ResultSet):
            return False

        def interval_to_tuple(interval):
            return (
                interval["interval_start"],
                interval["interval_end"],
                interval["interval_type"],
                interval["interval_ratio"],
            )

        self_set = set(interval_to_tuple(interval) for interval in self.intervals)
        other_set = set(interval_to_tuple(interval) for interval in other.intervals)

        return self_set == other_set

    def comparison_report(self, other: Any) -> list[str]:
        """Generate a detailed comparison report with side-by-side intervals."""
        if not isinstance(other, ResultSet):
            return ["Comparison is not valid: other object is not a ResultSet."]

        report = ["Comparison Report:"]
        report.append("")

        # Helper function to convert interval to a comparable key
        def interval_key(interval):
            return (
                interval["interval_start"],
                interval["interval_end"],
                interval["interval_type"],
                interval["interval_ratio"],
            )

        # Build dictionaries for quick lookup
        self_intervals_dict = {interval_key(i): i for i in self.intervals}
        other_intervals_dict = {interval_key(i): i for i in other.intervals}

        # Get all unique keys
        all_keys = set(self_intervals_dict.keys()).union(other_intervals_dict.keys())

        # Prepare combined intervals
        combined_intervals = []
        for key in sorted(all_keys):
            self_interval = self_intervals_dict.get(key)
            other_interval = other_intervals_dict.get(key)
            combined_intervals.append((self_interval, other_interval))

        # Define headers and column widths
        headers = [
            "Interval Start (left)",
            "Interval End (left)",
            "Type (left)",
            "Ratio (left)",
            "Interval Start (right)",
            "Interval End (right)",
            "Type (right)",
            "Ratio (right)",
        ]
        col_widths = [25, 25, 14, 13, 25, 25, 14, 13]

        # Create header row
        header_row = " | ".join(
            f"{header:<{width}}" for header, width in zip(headers, col_widths)
        )
        report.append(header_row)
        separator = "-" * (sum(col_widths) + len(headers) * 3 - 1)
        report.append(separator)

        # Function to format interval values
        def format_interval(interval):
            if interval is None:
                return [""] * 4
            return [
                interval["interval_start"].isoformat(),
                interval["interval_end"].isoformat(),
                interval["interval_type"],
                interval["interval_ratio"],
            ]

        # Add rows to the report
        for self_interval, other_interval in combined_intervals:
            self_values = format_interval(self_interval)
            other_values = format_interval(other_interval)
            row_values = self_values + other_values
            row = " | ".join(
                f"{str(value):<{width}}" for value, width in zip(row_values, col_widths)
            )
            report.append(row)

        return report

    def __repr__(self):
        return f"ResultSet({self.intervals})"
