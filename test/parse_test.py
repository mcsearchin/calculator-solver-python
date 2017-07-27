from unittest import TestCase
import parse

class ParseTest(TestCase):


  def setUp(self):
    self.subject = parse

  def test_throws_an_error_when_an_unknown_function_is_passed(self):
    self.assertRaises(ValueError, self.subject.parse, 'nonsense')

  def test_throws_an_error_when_a_partially_unknown_function_is_passed(self):
    self.assertRaises(ValueError, self.subject.parse, '+nonsense')

  def test_returns_a_function_that_adds_a_number(self):
  	resulting_function = self.subject.parse('+1')
  	
  	self.assertEquals(1, resulting_function(0))

  def test_returns_a_function_that_adds_a_two_digit_number(self):
  	resulting_function = self.subject.parse('+23')
  	
  	self.assertEquals(25, resulting_function(2))

  def test_returns_a_function_that_subtracts_a_number(self):
  	resulting_function = self.subject.parse('-7')
  	
  	self.assertEquals(-7, resulting_function(0))

  def test_returns_a_function_that_multiplies_a_number(self):
  	resulting_function = self.subject.parse('*2')
  	
  	self.assertEquals(8, resulting_function(4))

  def test_returns_a_function_that_divides_a_number(self):
  	resulting_function = self.subject.parse('/4')
  	
  	self.assertEquals(-3, resulting_function(-12))
