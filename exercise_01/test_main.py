"""Unit tests for the Robot class (exercise_01/main.py)."""

import unittest

from main import Robot


class TestRobotConstruction(unittest.TestCase):
    def test_starts_at_origin(self):
        robot = Robot(step_size=1)
        self.assertEqual(robot.get_current_pos(), (0, 0))

    def test_step_size_is_stored(self):
        robot = Robot(step_size=3)
        self.assertEqual(robot.step_size, 3)

    def test_rejects_zero_step_size(self):
        with self.assertRaises(ValueError):
            Robot(step_size=0)

    def test_rejects_negative_step_size(self):
        with self.assertRaises(ValueError):
            Robot(step_size=-2)

    def test_rejects_non_integer_step_size(self):
        with self.assertRaises(ValueError):
            Robot(step_size=1.5)


class TestSetStartPos(unittest.TestCase):
    def test_sets_position(self):
        robot = Robot(step_size=1)
        robot.set_start_pos(5, -3)
        self.assertEqual(robot.get_current_pos(), (5, -3))

    def test_clamped_if_boundaries_already_set(self):
        robot = Robot(step_size=1)
        robot.set_boundaries(max_x=4, max_y=4)
        robot.set_start_pos(-2, 10)
        self.assertEqual(robot.get_current_pos(), (0, 4))


class TestWalkUnbounded(unittest.TestCase):
    def test_single_step_each_direction(self):
        robot = Robot(step_size=1)
        robot.walk("U")
        self.assertEqual(robot.get_current_pos(), (0, 1))
        robot.walk("D")
        robot.walk("D")
        self.assertEqual(robot.get_current_pos(), (0, -1))
        robot.walk("R")
        robot.walk("R")
        self.assertEqual(robot.get_current_pos(), (2, -1))
        robot.walk("L")
        self.assertEqual(robot.get_current_pos(), (1, -1))

    def test_sequence_of_steps(self):
        robot = Robot(step_size=1)
        robot.walk("UUURRDDL")
        # U*3 -> (0,3); R*2 -> (2,3); D*2 -> (2,1); L -> (1,1)
        self.assertEqual(robot.get_current_pos(), (1, 1))

    def test_respects_step_size(self):
        robot = Robot(step_size=5)
        robot.walk("RU")
        self.assertEqual(robot.get_current_pos(), (5, 5))

    def test_lowercase_directions_are_accepted(self):
        robot = Robot(step_size=1)
        robot.walk("uurr")
        self.assertEqual(robot.get_current_pos(), (2, 2))

    def test_invalid_character_raises(self):
        robot = Robot(step_size=1)
        with self.assertRaises(ValueError):
            robot.walk("UX")

    def test_empty_string_is_a_no_op(self):
        robot = Robot(step_size=1)
        robot.walk("")
        self.assertEqual(robot.get_current_pos(), (0, 0))


class TestBoundaries(unittest.TestCase):
    def test_spec_example_clamped_upper_bound(self):
        # "If the boundaries are (4,4) and the robot received a command
        # that would move the robot to (3,5), it should return (3,4)."
        robot = Robot(step_size=1)
        robot.set_boundaries(max_x=4, max_y=4)
        robot.set_start_pos(3, 4)
        robot.walk("U")  # attempts (3, 5)
        self.assertEqual(robot.get_current_pos(), (3, 4))

    def test_walk_stops_at_boundary_mid_sequence(self):
        robot = Robot(step_size=1)
        robot.set_boundaries(max_x=2, max_y=2)
        robot.walk("RRRR")  # would reach x=4, but must stop at x=2
        self.assertEqual(robot.get_current_pos(), (2, 0))

    def test_lower_bound_is_zero(self):
        robot = Robot(step_size=1)
        robot.set_boundaries(max_x=5, max_y=5)
        robot.walk("LLLDDD")
        self.assertEqual(robot.get_current_pos(), (0, 0))

    def test_setting_boundaries_reclamps_existing_position(self):
        robot = Robot(step_size=1)
        robot.walk("RRRRRUUUUU")  # (5, 5)
        robot.set_boundaries(max_x=2, max_y=2)
        self.assertEqual(robot.get_current_pos(), (2, 2))

    def test_negative_boundary_rejected(self):
        robot = Robot(step_size=1)
        with self.assertRaises(ValueError):
            robot.set_boundaries(max_x=-1, max_y=3)

    def test_boundary_of_zero_pins_robot_to_origin(self):
        robot = Robot(step_size=1)
        robot.set_boundaries(max_x=0, max_y=0)
        robot.walk("RRUU")
        self.assertEqual(robot.get_current_pos(), (0, 0))


if __name__ == "__main__":
    unittest.main()
