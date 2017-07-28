import parse

def find_steps_to_solve(initial_value, desired_value, number_of_operations, allowed_operations):
  working_value = initial_value
  steps = []
  for index in range(number_of_operations):
    operation = parse.parse_operation(allowed_operations[0])
    working_value = operation(working_value)
    steps.append(allowed_operations[0])
    if working_value == desired_value:
      return steps

  raise ValueError(
    'Unable to calculate %s from %s in %s steps with the provided operations: %s' 
    % (desired_value, initial_value, number_of_operations, allowed_operations)
  )
