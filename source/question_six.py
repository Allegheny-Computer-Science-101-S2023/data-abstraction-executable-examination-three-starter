"""Question six for an executable examination."""

from typing import Callable
from typing import List
from typing import Tuple

# Question 6a. {{{

# Instructions:
# Implement the requested function so that it operates according to the function description

# Function description for compute_cube:
# The function compute_cube should:
# --> Accept as input one int value called input_one
# --> Use any appropriate approach to compute and return the cube of that number
# --> For instance, if input_one is equal to 1 then this function would return 1
# --> For instance, if input_one is equal to 2 then this function would return 8

# Instructions:
# Fix the defect(s) in the provided function so that it meets the function description

# Function description for apply_to_each_part_a:
# The function apply_to_each_part_a should:
# --> Accept as input a Callable function named function_to_call that accepts an input as an int and produces an int
# --> Accepts as input a list of int values called data_list
# --> Calls the function_to_call for each of the values inside of the data_list
# --> Replaces the current value at an index of data_list with the new value that was output from function_to_call
# --> Returns the data_list so that it can be displayed in the program's output

# Here is an example of the input and expected output for this function:
# Function call with inputs: apply_to_each_part_a([1, 2, 3], compute_cube)
# Final expected output: [1, 8, 27]


def compute_cube(input_one: int) -> int:
    """Use any approach that can cube an input number of type int."""
    cube_output = 0
    return cube_output


def apply_to_each_part_a(data_list: List[int], function_to_call: Callable[[int], int]) -> List[int]:
    """Apply the provided function to each of the values inside of the list."""
    for i in range(len(data_list)):
        data_list[i] = function_to_call(data_list[i - 1])
    return data_list


def question_six_a():
    """Run question six-a."""
    # Do not edit this function
    separator = " / "
    question_six_output_a = str(apply_to_each_part_a([1, 2, 3], compute_cube))
    question_six_output_a = question_six_output_a + separator + str(apply_to_each_part_a([4, 5, 6], compute_cube))
    question_six_output_a = question_six_output_a + separator + str(apply_to_each_part_a([0, 0, 0], compute_cube))
    question_six_output_a = question_six_output_a + separator + str(apply_to_each_part_a([1, 1, 1], compute_cube))
    return question_six_output_a

# }}}

# Question 6b. {{{

# Instructions:
# Implement the requested function so that it operates according to the function description

# Function description for compute_halved_number:
# The function compute_halved_number should:
# --> Accept as input one int value called input_one
# --> Use any appropriate approach to compute one-half of this number, rounding down and returning an int value
# --> For instance, if input_one is equal to 2 then this function would return 1
# --> For instance, if input_one is equal to 8 then this function would return 4
# --> For instance, if input_one is equal to 7 then this function would return 3

# Instructions:
# Repair the function so that it meets the following function description

# Function description for apply_to_each_part_b:
# The function apply_to_each_part_b should:
# --> Accept as input a Callable function named function_to_call that accepts an input as an int and produces an int
# --> Accepts as input a List of int values called data_list
# --> Calls the function_to_call for each of the values inside of the data_list
# --> Replaces the current value at an index of data_list with the new value that was output from function_to_call
# --> Returns the data_list so that it can be displayed in the program's output

# Note that apply_to_each_part_a and apply_to_each_part_b may have different
# defects in them even though they are designed to perform the same operation

# Here is an example of the input and expected output for this function:
# Function call with inputs: apply_to_each_part_b([2, 4, 8], compute_halved_number)
# Final expected output: [1, 2, 4]

# Here is another example of the input and expected output for this function:
# Function call with inputs: apply_to_each_part_b([3, 5, 7], compute_halved_number)
# Final expected output: [1, 2, 3]


def compute_halved_number(input_one: int) -> int:
    """Halve (i.e., divide by two) any provided int number, rounding down to the closest int value."""
    halved_value = int(input_one / 2)
    return halved_value


def apply_to_each_part_b(data_list: List[int], function_to_call: Callable[[int], int]) -> List[int]:
    """Apply the provided function to each of the values inside of the list."""
    i = 0
    data_list[i] = function_to_call(data_list[i])
    return data_list


def question_six_b():
    """Run question six-a."""
    # Do not edit this function
    separator = " / "
    question_six_output_b = str(apply_to_each_part_b([2, 4, 8], compute_halved_number))
    question_six_output_b = question_six_output_b + separator + str(apply_to_each_part_b([3, 5, 7], compute_halved_number))
    return question_six_output_b


# }}}

# Question 6c. {{{

# Instructions:
# Implement the following function so that it produces output
# according to the following function description

# Function description:
# The function determine_relationship should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is less than input_two
#     then the function should return a tuple containing (input_one, input_two, "<")
# --> If the value in input_one is greater than input_two
#     then the function should return a tuple containing (input_one, input_two, ">")
# --> If the value in input_one is exactly equal to input_two
#     then the function should return a tuple containing (input_one, input_two, "=")

# For instance, if the function is provided with the following input it
# will produce the specified output:
# --> Input one = 12, Input two = 10 produces the output (12, 10, '>')
# --> Input one = 10, Input two = 12 produces the output (10, 12, '<')
# --> Input one = 10, Input two = 10 produces the output (10, 10, '=')


def determine_relationship(input_one: int, input_two: int) -> Tuple[int, int, str]:
    """Determine the numerical relationship between the two input values."""
    return (input_one, input_two, "")


def question_six_c():
    """Run question six-b."""
    # Do not edit this function
    separator = " / "
    question_six_output_b = str(determine_relationship(12, 10))
    question_six_output_b = question_six_output_b + separator + str(determine_relationship(3, 9))
    question_six_output_b = question_six_output_b + separator + str(determine_relationship(2, 2))
    return question_six_output_b

# }}}

# Do not edit any of the source code below this line


def run_question_six():
    """Run all of the subquestions in question six."""
    # call the function for question six-a
    output = question_six_a()
    print(output)
    # call the function for question six-b
    output = question_six_b()
    print(output)
    # call the function for question six-c
    output = question_six_c()
    print(output)


if __name__ == "__main__":
    run_question_six()
