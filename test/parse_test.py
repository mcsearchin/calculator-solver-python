from unittest import TestCase
import parse

class ParseTest(TestCase):

  def setUp(self):
    subject = parse

  def test_throws_an_error_when_an_unknown_function_is_passed(self):
    self.assertRaises(ValueError, parse.parse, 'nonsense')

  def test_returns_a_function_that_adds_a_number(self):
  	add_function = parse.parse('+1')
  	
  	self.assertEquals(1, add_function(0))

  def test_returns_a_function_that_adds_a_different_number(self):
  	add_function = parse.parse('+2')
  	
  	self.assertEquals(4, add_function(2))  	