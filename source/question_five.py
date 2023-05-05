"""Question five for an executable examination."""

from typing import List

# Question 5a. {{{

# Instructions:
# Implement the requested function so that it operates in the specified fashion

# Function description:
# The function compute_repeated_multiplication should:
# --> Accept as input an int value called input_one that is the number that will be multiplied
# --> Accept as input an int value called multiply_count that is the number of multiplies to perform
# --> Using any appropriate approach compute and return the the input_one value
#     multiplied by itself a total of multiply_count times
# --> For instance, if input_one is equal to 1 and multiply_count is 5
#     then this function would return 1
# --> For instance, if input_one is equal to 2 and multiply_count is 3
#     then this function would return 8


def compute_repeated_multiplication(input_one: int, multiply_count: int) -> int:
    """Use any approach that can multiple an input number repeatedly."""
    count = 0
    running_multiplication = 1
    return running_multiplication


def question_five_a():
    """Run question five-a."""
    # Do not edit this function
    space = " "
    question_five_output_a = str(compute_repeated_multiplication(1, 3))
    question_five_output_a = question_five_output_a + space + str(compute_repeated_multiplication(2, 3))
    question_five_output_a = question_five_output_a + space + str(compute_repeated_multiplication(3, 3))
    return question_five_output_a

# }}}

# Question 5b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function get_maximum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is greater than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two


def get_maximum(input_one: int, input_two: int) -> int:
    """Return the maximum value of two input values."""
    if input_one < input_two:
        return input_one
    return input_two


def question_five_b():
    """Run question five-b."""
    # Do not edit this function
    space = " "
    question_five_output_b = str(get_maximum(12, 10))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 9))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 3))
    return question_five_output_b

# }}}

# Question 5c. {{{

# Instructions:
# Implement the following function so that it meets the following description

# Function description:
# The function def determine_is_subset_or_equals should:
# --> Accept as input two lists of integer values, that may potentially contain duplicate values
# --> Determine whether or not the first list is a subset of the second list
# --> When the subset property holds, the functions should return the value of True;
#     otherwise, it should return the value of False.
# --> When the first set is equal to the second set it should also return True

# For instance, if the function receives the inputs:
# [12, 10] and [9, 10, 11]
# then it would produce as output:
# False

# Note that in this example the use of the starting and ending brackets (i.e., [ and ])
# designates that the integer values are contained inside of a list


def determine_is_subset_or_equals(list_one: List, list_two: List) -> bool:
    """Determine whether or not the contents of the first list are a subset of the second list."""
    return True


def question_five_c():
    """Run question five-c."""
    # Do not edit this function
    separator = " / "
    question_five_output_c = str(determine_is_subset_or_equals([12, 10], [9, 10, 11]))
    question_five_output_c = question_five_output_c + separator + str(determine_is_subset_or_equals([1, 2, 3], [9, 10, 11]))
    question_five_output_c = question_five_output_c + separator + str(determine_is_subset_or_equals([2, 2, 3], [1, 2, 3]))
    question_five_output_c = question_five_output_c + separator + str(determine_is_subset_or_equals([1, 2, 3], [1, 2, 3]))
    return question_five_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_five():
    """Run all of the subquestions in question five."""
    # call the function for question five-a
    output = question_five_a()
    print(output)
    # call the function for question five-b
    output = question_five_b()
    print(output)
    # call the function for question five-c
    output = question_five_c()
    print(output)


if __name__ == "__main__":
    run_question_five()
