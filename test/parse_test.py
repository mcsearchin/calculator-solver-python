from unittest import TestCase
import parse

class ParseTest(TestCase):

  def setUp(self):
    self.subject = parse

  def test_raises_an_error_when_an_unknown_function_is_passed(self):
    self.assertRaises(ValueError, self.subject.parse_operation, 'nonsense')

  def test_raises_an_error_when_a_partially_unknown_function_is_passed(self):
    self.assertRaises(ValueError, self.subject.parse_operation, '+nonsense')

  def test_parses_a_function_that_adds_a_number(self):
  	resulting_function = self.subject.parse_operation('+1')
  	
  	self.assertEquals(1, resulting_function(0))

  def test_parses_a_function_that_adds_a_two_digit_number(self):
    resulting_function = self.subject.parse_operation('+23')
    
    self.assertEquals(25, resulting_function(2))

  def test_parses_a_function_that_adds_a_negative_number(self):
    resulting_function = self.subject.parse_operation('+-3')
    
    self.assertEquals(-1, resulting_function(2))

  def test_parses_a_function_that_subtracts_a_number(self):
  	resulting_function = self.subject.parse_operation('-7')
  	
  	self.assertEquals(-7, resulting_function(0))

  def test_parses_a_function_that_multiplies_a_number(self):
  	resulting_function = self.subject.parse_operation('*2')
  	
  	self.assertEquals(8, resulting_function(4))

  def test_parses_a_function_that_divides_a_number(self):
  	resulting_function = self.subject.parse_operation('/4')
  	
  	self.assertEquals(-3, resulting_function(-12))

  def test_parses_a_function_that_truncates_the_last_digit(self):
    resulting_function = self.subject.parse_operation('<<')

    self.assertEquals(78, resulting_function(789))

  def test_parsed_truncating_function_also_removes_digits_after_the_decimal_point(self):
    resulting_function = self.subject.parse_operation('<<')

    self.assertEquals(7, resulting_function(78.9))

  def test_parses_a_function_that_flips_the_sign_of_a_number(self):
    resulting_function = self.subject.parse_operation('+/-')

    self.assertEquals(1, resulting_function(-1))
    self.assertEquals(-1, resulting_function(1))
