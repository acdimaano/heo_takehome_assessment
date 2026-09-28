"""
Exercise 02 — best_average_grade.

Given a list of (student_name, score) tuples — where a student may
appear multiple times — find the student with the highest average
score.
"""

import math
from typing import List, Tuple, Union

Score = Tuple[str, float]
Result = Union[Tuple[str, int], int]


def best_average_grade(scores: List[Score]) -> Result:
    """
    Return (student_name, floor(average_score)) for the student with the
    highest average score across all their entries in `scores`.

    :param scores: a list of (student_name, score) tuples. A student may
        appear more than once; scores may be positive or negative.
    :return: a ``(name, average)`` tuple for the best-performing
        student, or ``0`` if `scores` is empty.
    """
    if not scores:
        return 0

    totals = {}
    counts = {}
    first_seen_order = []

    for name, score in scores:
        if name not in totals:
            totals[name] = 0
            counts[name] = 0
            first_seen_order.append(name)
        totals[name] += score
        counts[name] += 1

    best_name = None
    best_avg = None
    for name in first_seen_order:
        avg = math.floor(totals[name] / counts[name])
        if best_avg is None or avg > best_avg:
            best_avg = avg
            best_name = name

    return best_name, best_avg


if __name__ == "__main__":
    example = [("Alice", 10), ("John", 10), ("Bob", 11), ("Alice", 13), ("Bob", 1)]
    name, avg = best_average_grade(example)
    print(f"{name}, {avg}")  # -> Alice, 11
