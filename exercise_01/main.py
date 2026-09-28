"""
Exercise 01 — Robot class.

A Robot lives on a 2D grid, starts at position (0, 0), and moves one
"step" at a time in the direction it's told to walk. An optional
rectangular boundary can be set; once set, the robot's position is
always clamped so it never reports (or holds) a position outside it.
"""

from typing import Dict, Optional, Tuple


class Robot:
    """A robot that walks on an optionally-bounded two dimensional integer grid."""

    # Map each direction character to an (dx, dy) unit vector. Up, Down, Left, Riight.
    _DIRECTIONS: Dict[str, Tuple[int, int]] = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    def __init__(self, step_size: int):
        """
        Create a robot at origin (0, 0) with no boundaries set.

        :param step_size: the distance moved per direction character in
            `walk`. Must be a positive integer.
        """
        if not isinstance(step_size, int) or isinstance(step_size, bool) or step_size <= 0:
            raise ValueError("Step must be a positive integer!")

        self._step_size = step_size
        self._x_pos = 0
        self._y_pos = 0
        self._max_x: Optional[int] = None
        self._max_y: Optional[int] = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def step_size(self) -> int:
        """The number of grid units moved/step."""
        return self._step_size

    def set_start_pos(self, x: int, y: int) -> None:
        """Place the robot at (x, y), clamped to any active boundaries."""
        self._x_pos = x
        self._y_pos = y
        self._clamp_to_boundaries()

    def set_boundaries(self, max_x: int, max_y: int) -> None:
        """
        This method sets the boundaries of the robot. If during the
        movement, the robot goes out of the boundaries, it should be
        stopped.

        The valid region is ``0 <= x <= max_x`` and ``0 <= y <= max_y``.
        If the robot's current position is already outside the new
        boundaries, it is immediately clamped back inside them.
        """
        if max_x < 0 or max_y < 0:
            raise ValueError("X and Y must be positive value!")

        self._max_x = max_x
        self._max_y = max_y
        self._clamp_to_boundaries()

    def walk(self, direction: str) -> None:
        """
        This method walks the robot using a string to represent the
        sequence of steps. The string should be a sequence of the
        following characters:
            L => Left
            R => Right
            U => Up
            D => Down

        This method uses the `step_size` attribute to calculate the
        distance to move for each character. If a boundary is set, the
        robot stops at the edge as soon as a step would cross it, rather
        than overshooting and being clamped back afterwards.

        :raises ValueError: if `direction` contains any character other
            than L, R, U, D (case-insensitive).
        """
        for char in direction:
            key = char.upper()
            if key not in self._DIRECTIONS:
                raise ValueError(
                    f"Invalid direction character: {char!r}. "
                    "Expected one of 'L', 'R', 'U', 'D'."
                )
            dx, dy = self._DIRECTIONS[key]
            self._x_pos += dx * self._step_size
            self._y_pos += dy * self._step_size
            self._clamp_to_boundaries()

    def get_current_pos(self) -> Tuple[int, int]:
        """
        This method returns the current position of the robot. If the
        robot was just created, it returns the starting position (0, 0).
        This method respects any boundaries set by `set_boundaries`: if
        the stored position is outside them, the returned coordinate is
        clamped back inside first.
        """
        self._clamp_to_boundaries()
        return (self._x_pos, self._y_pos)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _clamp_to_boundaries(self) -> None:
        """Clamp the stored position into [0, max_x] x [0, max_y]."""
        if self._max_x is not None:
            self._x_pos = max(0, min(self._x_pos, self._max_x))
        if self._max_y is not None:
            self._y_pos = max(0, min(self._y_pos, self._max_y))

    def __repr__(self) -> str:
        return (
            f"Robot(step_size={self._step_size}, "
            f"pos=({self._x_pos}, {self._y_pos}), "
            f"boundaries=({self._max_x}, {self._max_y}))"
        )


if __name__ == "__main__":
    # Small runnable demo, mirroring the boundary example from the pdf file.
    robot = Robot(step_size=1)
    robot.set_boundaries(max_x=4, max_y=4)
    robot.set_start_pos(3, 4)
    robot.walk("U")  # would move to (3, 5); clamped to (3, 4)
    print("Position after walking 'U' past the boundary:", robot.get_current_pos())
    assert robot.get_current_pos() == (3, 4)
