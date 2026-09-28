# Exercise 01 — Robot

## Problem

Complete the `Robot` class: a robot that starts at `(0, 0)` on a two dimensional
grid, can be moved with `walk(direction)` using a string of `L`/`R`/`U`/`D`
characters, and can optionally have a rectangular boundary set with
`set_boundaries(max_x, max_y)` that it must never move or report a
position outside of.

## Key design decisions

The original method stubs only sketched the class — see the module
docstring at the top of `main.py` for the full reasoning, summarised
here:

- **Boundary shape.** `set_boundaries(max_x, max_y)` defines the valid
  region as `0 <= x <= max_x` and `0 <= y <= max_y`. The lower bound of
  0 isn't stated explicitly in the spec, but it's the only interpretation
  consistent with the robot starting at the origin and the one worked
  example given (boundaries `(4, 4)`, target `(3, 5)` → `(3, 4)`).
- **Eager, defensive clamping.** Every method that can change the
  position re-clamps immediately, and `get_current_pos` clamps again
  before returning — so the invariant "position is always inside the
  boundary" holds no matter which method was called last.
- **`walk` clamps per character**, not just once at the end of the
  string, so the robot "stops" exactly at the wall instead of
  overshooting and snapping back.
- Invalid `step_size` (not a positive int) and invalid characters passed
  to `walk` both raise `ValueError` instead of failing silently.

## How to run

```bash
# Run the demo (mirrors the spec's boundary example)
python3 main.py

# Run the tests
python3 -m unittest test_main.py -v
```

No external dependencies — everything here is Python standard library
(tested on Python 3.9+, but should work on any Python 3.7+).

## Test coverage

19 tests in `test_main.py` covering: construction/validation, unbounded
walking in all four directions (including multi-step sequences and
case-insensitivity), the exact example from the spec, boundary clamping
(upper bound, lower bound, mid-sequence stopping, re-clamping when
boundaries are set after the fact), and invalid input handling.
