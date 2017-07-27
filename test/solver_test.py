from unittest import TestCase
import solver

class SolverTest(TestCase):

  def setUp(self):
    self.subject = solver

  def test_solves_a_simple_single_operation_problem(self):
    moves = self.subject.solve(0, 1, 1, ['+1'])

    self.assertEquals(['+1'], moves)