from unittest import TestCase
import calculator_solver

class ApiTest(TestCase):

  def setUp(self):
    self.subject = calculator_solver

  def test_prints_solution_when_all_correct_arguments_are_specified(self):
  	result = self.subject.main(['-i', '0', '-d' '7', '-n', '3', '-o', '+1, *3,+4'])

  	self.assertEquals("Steps to solution: ['+1', '*3', '+4']", result)

  def test_prints_relevant_error_message_when_unknown_options_are_specified(self):
  	result = self.subject.main(['-x'])

  	self.assertTrue('option -x not recognized' in result)

  def test_prints_relevant_error_message_when_all_arguments_are_not_specified(self):
  	self.assertTrue('All arguments are required.' in self.subject.main(['-i', '0', '-d' '7', '-n', '3']))
  	self.assertTrue('All arguments are required.' in self.subject.main(['-i', '0', '-d' '7', '-o', '+1, *3,+4']))
  	self.assertTrue('All arguments are required.' in self.subject.main(['-i', '0', '-n', '3', '-o', '+1, *3,+4']))
  	self.assertTrue('All arguments are required.' in self.subject.main(['-d' '7', '-n', '3', '-o', '+1, *3,+4']))

  def test_prints_relevant_error_message_when_necessary_arguments_are_not_integers(self):
  	self.assertTrue('initial-value must be an integer.' in self.subject.main(['-i', '', '-d' '7', '-n', '3', '-o', '+1, *3,+4']))
  	self.assertTrue('desired-value must be an integer.' in self.subject.main(['-i', '0', '-d' 'x', '-n', '3', '-o', '+1, *3,+4']))
  	self.assertTrue('number-of-steps must be an integer.' in self.subject.main(['-i', '0', '-d' '7', '-n', '--', '-o', '+1, *3,+4']))

  def test_prints_error_messages_returned_by_the_solution_logic(self):
  	result = self.subject.main(['-i', '0', '-d' '7', '-n', '3', '-o', 'nonsense'])

  	self.assertTrue('Illegal operation : nonsense' in result)
