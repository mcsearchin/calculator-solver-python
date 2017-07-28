import parse

def find_steps_to_solve(initial_value, desired_value, number_of_steps, allowed_operations_set):
  solution = _attempt_to_solve(initial_value, desired_value, number_of_steps, [], allowed_operations_set)
  if solution:
    return solution
  else:
    raise ValueError(
      'Unable to calculate %s from %s in %s steps with the provided operations: %s' 
      % (desired_value, initial_value, number_of_steps, allowed_operations_set)
    )

def _attempt_to_solve(current_value, desired_value, number_remaining_steps, steps_so_far, allowed_operations_set):
  if number_remaining_steps < 1:
    return None

  for operation_string in allowed_operations_set:
    operation = parse.parse_operation(operation_string)
    new_value = operation(current_value)
    steps = steps_so_far + [operation_string]
    if new_value == desired_value:
      return steps
    else:
      possible_solution = _attempt_to_solve(new_value, desired_value, number_remaining_steps - 1, steps, allowed_operations_set)
      if possible_solution:
        return possible_solution
