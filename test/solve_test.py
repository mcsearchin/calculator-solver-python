from unittest import TestCase
import solve

class SolveTest(TestCase):

  def setUp(self):
    self.subject = solve

  def test_finds_steps_to_solve_a_single_operation_problem(self):
    steps = self.subject.find_steps_to_solve(0, 1, 1, ['+1'])

    self.assertEquals(['+1'], steps)

  def test_finds_steps_to_solve_a_multi_step_single_operation_problem(self):
    steps = self.subject.find_steps_to_solve(0, 2, 2, ['+1'])

    self.assertEquals(['+1', '+1'], steps)

  def test_finds_steps_to_solve_a_single_operation_problem_in_fewer_steps_than_provided(self):
    steps = self.subject.find_steps_to_solve(0, 1, 2, ['+1'])

    self.assertEquals(['+1'], steps)

  def test_raises_an_error_when_not_enough_steps_are_provided_to_solve_the_problem(self):
    self.assertRaises(ValueError, self.subject.find_steps_to_solve, 0, 3, 2, ['+1'])

  def test_finds_steps_to_solve_a_different_single_operation_problem(self):
    steps = self.subject.find_steps_to_solve(1, 3, 1, ['*3'])

    self.assertEquals(['*3'], steps)
