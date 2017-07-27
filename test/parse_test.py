from unittest import TestCase
import parse

class ParseTest(TestCase):

  def setUp(self):
    subject = parse

  def test_throws_an_error_when_an_unknown_function_is_passed(self):
    self.assertRaises(ValueError, parse.parse, 'nonsense')

  def test_throws_an_error_when_a_partially_unknown_function_is_passed(self):
    self.assertRaises(ValueError, parse.parse, '+nonsense')

  def test_returns_a_function_that_adds_a_number(self):
  	add_function = parse.parse('+1')
  	
  	self.assertEquals(1, add_function(0))

  def test_returns_a_function_that_adds_a_two_digit_number(self):
  	add_function = parse.parse('+23')
  	
  	self.assertEquals(25, add_function(2))

  def test_returns_a_function_that_subtracts_a_number(self):
  	add_function = parse.parse('-7')
  	
  	self.assertEquals(-7, add_function(0))
