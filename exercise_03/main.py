"""
Exercise 03 — longest_increase_sequence.
"""

from bisect import bisect_left
from typing import List


def longest_increase_sequence(nums: List[int]) -> int:
    """
    Return the length of the longest *contiguous* run of strictly
    increasing values in `nums` (i.e. a run where every element is
    strictly greater than the one before it). This is the
    interpretation that matches the exercise's two worked examples
    exactly — see the module docstring for why.

    Runs in O(n) time and O(1) extra space.

    :param nums: a list of comparable values (e.g. ints).
    :return: the length of the longest increasing run, or 0 for an
        empty list.
    """
    if not nums:
        return 0

    longest = 1
    current = 1
    for previous, current_value in zip(nums, nums[1:]):
        if current_value > previous:
            current += 1
        else:
            current = 1
        longest = max(longest, current)

    return longest


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Classic, *non-contiguous* Longest Increasing Subsequence: the length
    of the longest strictly increasing subsequence obtainable by
    deleting zero or more elements without reordering the rest.

    Provided as a bonus/alternative implementation in case this (rather
    than the contiguous version above) is what was intended — see the
    module docstring for the worked-example analysis that led to
    `longest_increase_sequence` being the primary implementation instead.

    Runs in O(n log n) time using the standard "patience sorting"
    technique (`tails[i]` holds the smallest possible tail value of an
    increasing subsequence of length `i + 1` seen so far).

    :param nums: a list of comparable values (e.g. ints).
    :return: the length of the longest increasing subsequence, or 0 for
        an empty list.
    """
    if not nums:
        return 0

    tails: List[int] = []
    for num in nums:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num

    return len(tails)


if __name__ == "__main__":
    example_a = [3, 4, 5, 1, 6]
    example_b = [1, 2, 3, 3, 3, 4]

    print("longest_increase_sequence(", example_a, ") =", longest_increase_sequence(example_a))
    print("longest_increase_sequence(", example_b, ") =", longest_increase_sequence(example_b))

    print(
        "longest_increasing_subsequence(", example_a, ") =",
        longest_increasing_subsequence(example_a),
        "(bonus/alternative, non-contiguous)",
    )
