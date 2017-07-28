from unittest import TestCase
import solver

class SolverTest(TestCase):

  def setUp(self):
    self.subject = solver

  def test_solves_a_simple_single_operation_problem(self):
    steps = self.subject.find_steps_to_solve(0, 1, 1, ['+1'])

    self.assertEquals(['+1'], steps)

  def test_solves_a_simple_multi_step_single_operation_problem(self):
    steps = self.subject.find_steps_to_solve(0, 2, 2, ['+1'])

    self.assertEquals(['+1', '+1'], steps)

