# Exercise 02 — best_average_grade

## Problem

Given a list of `(student_name, score)` tuples — a student may appear
more than once, and scores can be negative — return the student with
the highest average score. Non-integer averages are floored. An empty
input returns `0`.

## Key design decisions

- **Return shape.** The spec's example ("Returns: Alice, 11") is
  implemented as a `(name, average)` tuple, the natural return type for
  a function. `main.py`'s demo block also prints it as `Alice, 11` to
  match the pdf's exact wording.
- **`math.floor`, not `int()`.** These disagree for negative numbers —
  `int(-1.5) == -1` but `math.floor(-1.5) == -2` — and the pdf's
  "largest integer less than or equal to the average" is the `floor`
  definition. Since scores may be negative, this matters and is covered
  by a dedicated test.
- **Tie-breaking.** Not specified in the pdf, so ties are broken by
  whichever student *first appears* in the input list. This is
  deterministic and tested explicitly.

## How to run

```bash
# Run the demo (prints "Alice, 11" using the spec's example)
python3 main.py

# Run the tests
python3 -m unittest test_main.py -v
```

No external dependencies — standard library only.

## Test coverage

9 tests covering: the spec's own example, empty input, a student with a
single score, floor behaviour for both positive and negative averages,
picking the best *average* rather than the best *total*, tie-breaking,
and a slightly larger multi-student case.
