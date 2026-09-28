"""Unit tests for best_average_grade (exercise_02/main.py)."""

import unittest

from main import best_average_grade


class TestBestAverageGrade(unittest.TestCase):
    def test_spec_example(self):
        scores = [("Alice", 10), ("John", 10), ("Bob", 11), ("Alice", 13), ("Bob", 1)]
        self.assertEqual(best_average_grade(scores), ("Alice", 11))

    def test_empty_input_returns_zero(self):
        self.assertEqual(best_average_grade([]), 0)

    def test_single_student_single_score(self):
        self.assertEqual(best_average_grade([("Alice", 7)]), ("Alice", 7))

    def test_single_student_multiple_scores(self):
        # (4 + 5 + 6) / 3 = 5.0 -> floor 5
        self.assertEqual(best_average_grade([("Alice", 4), ("Alice", 5), ("Alice", 6)]), ("Alice", 5))

    def test_floor_rounds_down_not_towards_zero(self):
        # (10 + 11) / 2 = 10.5 -> floor 10 (not rounded to 11)
        self.assertEqual(best_average_grade([("Bob", 10), ("Bob", 11)]), ("Bob", 10))

    def test_negative_scores_use_floor_not_truncation(self):
        # (-1 + -2) / 2 = -1.5 -> floor(-1.5) == -2 (int(-1.5) would be -1)
        self.assertEqual(best_average_grade([("Carol", -1), ("Carol", -2)]), ("Carol", -2))

    def test_picks_highest_average_not_highest_total(self):
        # Bob has a higher total (100) but a much lower average than Alice.
        scores = [("Alice", 90), ("Alice", 90), ("Bob", 100), ("Bob", 0), ("Bob", 0)]
        self.assertEqual(best_average_grade(scores), ("Alice", 90))

    def test_tie_breaks_towards_first_appearance(self):
        # Alice and Bob both average 5; Alice appears first in the list.
        scores = [("Bob", 5), ("Alice", 5), ("Alice", 5), ("Bob", 5)]
        self.assertEqual(best_average_grade(scores), ("Bob", 5))

    def test_many_students(self):
        scores = [
            ("A", 100), ("B", 1), ("C", 50),
            ("A", 100), ("B", 1), ("C", 50),
        ]
        self.assertEqual(best_average_grade(scores), ("A", 100))


if __name__ == "__main__":
    unittest.main()
