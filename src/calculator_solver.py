import sys
from getopt import getopt, GetoptError
import solve

def main(argv):

  initial_value = None
  desired_value = None
  number_of_steps = None
  allowed_operation_strings = None
  error_string = ''

  try:
    opts, args = getopt(argv, 'i:d:n:o:', ['initial-value=', 'desired-value=', 'number-of-steps=', 'allowed-operations='])
  except GetoptError as error:
    return '%s%s' % (error, _get_usage_string())

  for opt, arg in opts:
    if opt in ('-i', '--initial-value'):
      initial_value = _get_int_value(arg)
      if initial_value is None:
        error_string += '\ninitial-value must be an integer.'

    elif opt in ('-d', '--desired-value'):
      desired_value = _get_int_value(arg)
      if desired_value is None:
        error_string += '\ndesired-value must be an integer.'

    elif opt in ('-n', '--number-of-steps'):
      number_of_steps = _get_int_value(arg)
      if number_of_steps is None:
        error_string += '\nnumber-of-steps must be an integer.'

    elif opt in ('-o', '--allowed-operations'):
      allowed_operation_strings = _split_operations_string(arg)

  if initial_value is None \
      or desired_value is None \
      or number_of_steps is None \
      or allowed_operation_strings is None:
    error_string += '\nAll arguments are required.'

  if error_string:
    return error_string + _get_usage_string()

  try:
    return 'Steps to solution: %s' % solve.find_steps_to_solve(initial_value, desired_value, number_of_steps, allowed_operation_strings)
  except Exception as error:
    return '%s%s' % (error, _get_usage_string())

def _get_int_value(string):
  try:
    return int(string)
  except ValueError:
    return None

def _split_operations_string(operations_string):
  operation_strings = operations_string.split(',')
  return [operation_string.strip() for operation_string in operation_strings]

def _get_usage_string():
  return '\n\nExample usage:' \
    '\npython src/calculator_solver.py -i 0 -d -4 -n 2 -o \'-5, +1\'' \
    '\n-i, --initial-value=       Self-explanatory' \
    '\n-d, --desired-value=       The desired calculated final value' \
    '\n-n, --number-of-steps=     The maximum number of operations that can be applied to get to the desire value.' \
    '\n-o, --allowed-operations=  The set of allowed operations.' \
    '\nAllowed operation values are +x, -x, *x, /x, ' \
    '\n<< (will truncate the last decimal place, i.e. 12 becomes 1), ' \
    '\nand x (will append to the existing numeric value, i.e. applying \'2\' to \'1\' results in \'12\')\n'


if __name__ == "__main__":
  print main(sys.argv[1:])