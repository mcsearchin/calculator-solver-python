import re

def parse(function_string):
  arithmetic = re.compile('^[+\-*/][0-9]+$')
  if (arithmetic.match(function_string)):
    operator = function_string[0:1]
    second_term = int(function_string[1:])

    return {
      '+': lambda value: value + second_term,
      '-': lambda value: value - second_term,
      '*': lambda value: value * second_term,
      '/': lambda value: value / second_term,
    }[operator]

  raise ValueError('Illegal function : %s' % function_string)

