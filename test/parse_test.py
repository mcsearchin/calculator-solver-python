from unittest import TestCase
import parse

class ParseTest(TestCase):

  def setUp(self):
    subject = parse

  def test_throws_an_error_when_an_unknown_function_is_passed(self):
    self.assertRaises(ValueError, parse.parse, 'nonsense')