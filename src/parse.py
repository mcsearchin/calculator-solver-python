import re

def parse(function_string):
  arithmetic = re.compile('^[+-][0-9]+$')
  if (arithmetic.match(function_string)):
    term = int(function_string[1:])
    if (function_string.startswith('+')):
      def add(value):
        return value + term
      return add
    else:
      def subtract(value):
        return value - term
      return subtract

  raise ValueError('Illegal function : %s' % function_string)