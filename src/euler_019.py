#!/usr/bin/env python

import datetime


def solver(
    start_year: int, end_year: int, month_day: int, week_day: str
) -> int:
    """Main solver of the task."""
    days = dict()
    days["Monday"] = 0
    days["Tuesday"] = 1
    days["Wednesday"] = 2
    days["Thursday"] = 3
    days["Friday"] = 4
    days["Saturday"] = 5
    days["Sunday"] = 6

    result = 0
    for i in range(start_year, end_year + 1):
        for j in range(1, 13):
            if datetime.date(i, j, month_day).weekday() == days[week_day]:
                result += 1
    return result


def main() -> None:
    """Print the solution."""
    print(solver(1901, 2000, 1, "Sunday"))


if __name__ == "__main__":
    main()
