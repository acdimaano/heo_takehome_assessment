"""Unit tests for longest_increase_sequence (exercise_03/main.py)."""

import unittest

from main import longest_increase_sequence, longest_increasing_subsequence


class TestLongestIncreaseSequenceSpecExamples(unittest.TestCase):
    """These two cases are taken directly from the exercise instructions."""

    def test_example_one(self):
        self.assertEqual(longest_increase_sequence([3, 4, 5, 1, 6]), 3)

    def test_example_two(self):
        self.assertEqual(longest_increase_sequence([1, 2, 3, 3, 3, 4]), 3)


class TestLongestIncreaseSequenceEdgeCases(unittest.TestCase):
    def test_empty_list_returns_zero(self):
        self.assertEqual(longest_increase_sequence([]), 0)

    def test_single_element(self):
        self.assertEqual(longest_increase_sequence([42]), 1)

    def test_all_strictly_increasing(self):
        self.assertEqual(longest_increase_sequence([1, 2, 3, 4, 5]), 5)

    def test_all_strictly_decreasing(self):
        self.assertEqual(longest_increase_sequence([5, 4, 3, 2, 1]), 1)

    def test_all_equal_values(self):
        # Not strictly increasing, so every run has length 1.
        self.assertEqual(longest_increase_sequence([7, 7, 7, 7]), 1)

    def test_run_in_the_middle_is_the_longest(self):
        self.assertEqual(longest_increase_sequence([9, 1, 2, 3, 4, 0]), 4)

    def test_negative_numbers(self):
        self.assertEqual(longest_increase_sequence([-5, -3, -1, -4, -2, 0]), 3)


class TestLongestIncreasingSubsequenceBonus(unittest.TestCase):
    """Sanity checks for the classic non-contiguous alternative."""

    def test_empty_list_returns_zero(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_classic_example(self):
        # Well-known example (LeetCode #300): LIS is [2, 3, 7, 101], length 4.
        self.assertEqual(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_can_exceed_the_contiguous_version(self):
        nums = [3, 4, 5, 1, 6]
        self.assertEqual(longest_increasing_subsequence(nums), 4)  # 3,4,5,6
        self.assertEqual(longest_increase_sequence(nums), 3)


if __name__ == "__main__":
    unittest.main()
