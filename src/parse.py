import re

def parse_operation(operation_string):
  arithmetic = re.compile('^[+\-*/][0-9]+$')
  if (arithmetic.match(operation_string)):
    operator = operation_string[0:1]
    second_term = float(operation_string[1:])

    return {
      '+': lambda value: value + second_term,
      '-': lambda value: value - second_term,
      '*': lambda value: value * second_term,
      '/': lambda value: value / second_term,
    }[operator]

  raise ValueError('Illegal operation : %s' % operation_string)

