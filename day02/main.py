from typing import List
from enum import Enum

INPUT_FILE = "input.txt"

reports: List[List[int]] = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        report = list(map(int, line.split(" ")))
        reports.append(report)


class ReportType(Enum):
    DECREASING = 0
    INCREASING = 1


def check_all(report, dampener):
    if dampener:
        for idx in range(len(report)):
            res = check_safety(report[:idx] + report[idx + 1 :])
            if res == 1:
                return 1
    return 0


def check_safety(report: List[int], dampener: bool = False):

    if report[1] < report[0]:
        type = ReportType.DECREASING
    elif report[1] > report[0]:
        type = ReportType.INCREASING
    else:
        return check_all(report, dampener)

    for idx in range(len(report) - 1):
        diff = report[idx + 1] - report[idx]
        if 1 <= abs(diff) <= 3:
            if diff > 0 and type == ReportType.INCREASING:
                continue
            if diff < 0 and type == ReportType.DECREASING:
                continue
            else:
                return check_all(report, dampener)
        else:
            return check_all(report, dampener)
    return 1


safe_report_count = 0

for report in reports:
    if check_safety(report, True) == 1:
        safe_report_count += 1

print("Safe report count:", safe_report_count)
