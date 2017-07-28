import parse

def find_steps_to_solve(initial_value, desired_value, number_of_operations, allowed_operations_set):
  steps = _attempt_to_solve(initial_value, desired_value, number_of_operations, allowed_operations_set)
  if steps:
    return steps

  steps = _attempt_to_solve(initial_value, desired_value, number_of_operations, allowed_operations_set[::-1])
  if steps:
    return steps
    
  raise ValueError(
    'Unable to calculate %s from %s in %s steps with the provided operations: %s' 
    % (desired_value, initial_value, number_of_operations, allowed_operations_set)
  )

def _attempt_to_solve(initial_value, desired_value, number_of_operations, allowed_operations_set):
  working_value = initial_value
  steps = []
  for index in range(number_of_operations):
    op_index = index if index < len(allowed_operations_set) else len(allowed_operations_set) - 1
    operation_string = allowed_operations_set[op_index]
    operation = parse.parse_operation(operation_string)
    working_value = operation(working_value)
    steps.append(operation_string)
    if working_value == desired_value:
      return steps

