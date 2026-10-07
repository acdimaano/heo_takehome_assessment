# HEO Take-Home Assessment — Solutions

This repository contains solutions to the three coding exercises from
the HEO take-home assessment:

- **`exercise_01/`** — a completed `Robot` class (movement + boundaries)
- **`exercise_02/`** — `best_average_grade`, finding the student with the
  highest average test score
- **`exercise_03/`** — `longest_increase_sequence`, finding the longest
  increasing run in a list (see that exercise's README for an important
  note on an ambiguity in the spec)

Each exercise is fully self-contained in its own folder (`main.py` +
`test_main.py` + its own `README.md` with exercise-specific design notes)
so nothing leaks between them.

## How to run and set up

**Requirements:** Python 3.7+ and nothing else — every solution uses
only the standard library, so there's no `requirements.txt` and no
`pip install` needed.

**Run the tests for a single exercise:**

```bash
cd exercise_01   # or exercise_02 / exercise_03
python3 -m unittest test_main.py -v
```

**Run a single exercise's demo** (each `main.py` is directly runnable
and prints a small worked example):

```bash
cd exercise_02
python3 main.py
# -> Alice, 11
```

## Things I'd improve / issues I'd address as a Software Engineer

- **Exercise 01 (Robot):** the boundary's lower bound (fixed at 0 in
  this implementation) is an assumption, not something the spec states
  explicitly. In a real codebase I'd get this confirmed by whoever wrote
  the spec rather than guessing, and I'd promote it to an explicit
  constructor parameter (e.g. `min_x`/`min_y`, defaulting to 0) so it's
  configurable instead of hard-coded.
- **Exercise 01 (Robot):** `walk` currently raises on the first invalid
  character it finds, after having already applied any valid characters
  before it — so a partially-invalid string leaves the robot moved. A
  stricter version might validate the whole string upfront and raise
  before moving at all; I'd want to know which behaviour the caller
  actually expects.
- **Exercise 02:** tie-breaking behaviour (first-appearance wins) is my
  own assumption, made explicit and tested, but not specified in the
  brief — worth confirming with a product owner in a real scenario
  rather than a take-home.
- **Exercise 03:** the biggest open item. As documented in
  `exercise_03/README.md`, the spec's own worked examples only make
  sense under a *contiguous* "longest increasing run" reading, despite
  the function being named after the classic *non-contiguous* Longest
  Increasing Subsequence problem and the brief explicitly saying the
  list "doesn't need to be contiguous". I implemented the interpretation
  that matches the given examples, and included the classic
  non-contiguous algorithm as a separate, tested, bonus function in case
  that's what was actually wanted. This is exactly the kind of
  ambiguity I'd raise with whoever wrote the ticket before writing any
  code, rather than silently picking one reading.
- **General:** none of the three solutions have type-checking (e.g.
  `mypy`) or a linter (e.g. `ruff`/`flake8`) wired up. For a short
  take-home I judged that to be overkill, but in a real repository I'd
  add both plus a CI workflow that runs the tests (and the linter) on
  every push.
- **General:** all three modules are single-file for simplicity, which
  is appropriate at this size. If any of them grew (e.g. more grid
  shapes for the Robot, more grading rules for `best_average_grade`),
  I'd split validation, core logic, and the CLI/demo entry point into
  separate modules.

## External resources & AI assistance

- The three exercises are otherwise standard, well-known problem types
  (a simple stateful class, a grouping/aggregation problem, and a
  classic DSA sequence problem), implemented from first principles —
  no external code, snippets, or Stack Overflow answers were copied.
- **Exercise 03** involved a genuine judgement call rather than a
  "hint" — see the dedicated write-up in `exercise_03/README.md` for
  the worked-example analysis that led to implementing the contiguous
  interpretation as primary, with the classic non-contiguous LIS
  algorithm (patience sorting / `bisect_left` over a `tails` array, a
  well-known O(n log n) technique for that problem) included as a
  documented, tested alternative.
- `math.floor` (Exercise 02) and `bisect.bisect_left` (Exercise 03,
  bonus function) are both standard-library functions used in their
  ordinary, well-documented way — no external references needed beyond
  the Python docs.
