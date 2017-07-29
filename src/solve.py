import parse

def find_steps_to_solve(initial_value, desired_value, number_of_steps, allowed_operation_strings):
  operations_dictionary = _parse_operations(allowed_operation_strings)
  
  solution = _attempt_to_solve(initial_value, desired_value, number_of_steps, [], operations_dictionary)
  if solution:
    return solution
  else:
    raise ValueError(
      'Unable to calculate %s from %s in %s steps with the provided operations: %s' 
      % (desired_value, initial_value, number_of_steps, allowed_operation_strings)
    )

def _parse_operations(operation_strings):
  operations_dictionary = {}
  for operation_string in operation_strings:
    operations_dictionary[operation_string] = parse.parse_operation(operation_string)

  return operations_dictionary  

def _attempt_to_solve(current_value, desired_value, number_remaining_steps, steps_so_far, operations_dictionary):
  if number_remaining_steps < 1:
    return None

  for operation_string, operation in operations_dictionary.items():
    new_value = operation(current_value)
    steps = steps_so_far + [operation_string]

    if new_value == desired_value:
      return steps
    else:
      possible_solution = _attempt_to_solve(new_value, desired_value, number_remaining_steps - 1, steps, operations_dictionary)
      if possible_solution:
        return possible_solution
