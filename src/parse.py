import re

def parse_operation(operation_string):

  if _is_arithmetic_operation(operation_string):
    return _generate_arithmetic_function(operation_string)
  if _is_appending_operation(operation_string):
    return _generate_appending_function(operation_string)
  if '<<' == operation_string:
    return lambda value: int(value) / 10
  if '+/-' == operation_string:
    return lambda value: int(value) * -1

  raise ValueError('Illegal operation : %s' % operation_string)

def _is_arithmetic_operation(operation_string):
  return re.compile('^[+\-*/][\-]?[0-9]+$').match(operation_string)

def _generate_arithmetic_function(operation_string):
  operator = operation_string[0:1]
  second_term = float(operation_string[1:])

  return {
    '+': lambda value: value + second_term,
    '-': lambda value: value - second_term,
    '*': lambda value: value * second_term,
    '/': lambda value: value / second_term,
  }[operator]

def _is_appending_operation(operation_string):
  return re.compile('^[0-9]+$').match(operation_string)

def _generate_appending_function(operation_string):
  places_to_shift = len(operation_string)
  number_to_append = int(operation_string)
  return lambda value: int(value) * (10**places_to_shift) + number_to_append
