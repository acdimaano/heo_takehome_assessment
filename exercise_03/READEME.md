# Exercise 03 — longest_increase_sequence (LIS)

## Problem

Given a list, return the length of the longest increasing sequence it
contains.

## ⚠️ A genuine ambiguity in the pdf exercise specifications, and how it was resolved

This is the most important thing to read in this whole submission.

The exercise names the function after the classic "Longest Increasing
**Subsequence**" problem and says the list "doesn't need to be
contiguous" — normally that means you can freely skip elements as long
as the ones you keep are strictly increasing (the standard,
non-contiguous definition, solvable in O(n log n)).

But working through the exercise's **own worked examples** shows that
only a **contiguous** interpretation (the longest run of strictly
increasing values *in a row*) actually reproduces the stated answers:

| Input                | Spec says | Classic non-contiguous LIS.             | Contiguous run  |
|----------------------|-----------|-----------------------------------------|------------------|
| `[3, 4, 5, 1, 6]`    | **3**.    | 4 → `3,4,5,6` (skipping the `1`)        | 3 → `[3,4,5]` ✅ |
| `[1, 2, 3, 3, 3, 4]` | **3**.    | 4 → `1,2,3,4` (skipping duplicate `3`s) | 3 → `[1,2,3]` ✅ |

In both cases, the classic non-contiguous definition gives a longer
answer (4) than the one the spec states (3). Since the worked examples
are the most concrete, checkable part of the spec — more concrete than
the word "contiguous" in a single sentence — **`longest_increase_sequence`
implements the contiguous "longest increasing run" definition**, which
reproduces both examples exactly.

In case the non-contiguous version is what was actually intended, the
classic algorithm is *also* provided, clearly separated, as
`longest_increasing_subsequence` (O(n log n), patience-sorting method),
with its own tests including the textbook LeetCode #300 example.

If this assumption is wrong, swapping which function `main.py`'s
`__main__` block treats as "the answer" is a one-line change — the hard
part (having a correct, tested implementation of both definitions) is
already done.

## How to run

```bash
# Run the demo (prints both example results, plus the bonus function)
python3 main.py

# Run the tests
python3 -m unittest test_main.py -v
```

No external dependencies — standard library only (`bisect`).

## Test coverage

12 tests: the two exact spec examples, standard edge cases (empty list,
single element, all increasing, all decreasing, all-equal values,
negative numbers, a run in the middle of the list), and three sanity
checks on the bonus non-contiguous implementation — including one test
that explicitly demonstrates the two functions disagreeing on
`[3, 4, 5, 1, 6]` (3 vs. 4), which is the crux of the ambiguity above.
