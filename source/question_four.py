"""Question four for an executable examination."""

from typing import List

# Question 4a. {{{

# Instructions:
# Implement this function so that it operates in the specified fashion

# Function description:
# The function compute_remainder should:
# --> Accept as input two int values called value_one and value_two
# --> Compute the remainder of the division value_one / value_two
# --> For instance, if value_one is equal to 10 and value_two is
#     equal to 2 then this function would return the remainder of 0
# --> Alternatively, if value_one is equal to 10 and value_two is
#     equal to 3 then this function would return the remainder of 1


def compute_remainder(value_one: int, value_two: int) -> int:
    """Compute the remainder of the two provided int values."""
    return 0


def question_four_a():
    """Run question four-a."""
    # Do not edit this function
    space = " "
    question_four_output_a = str(compute_remainder(10, 2))
    question_four_output_a = question_four_output_a + space + str(compute_remainder(9, 3))
    question_four_output_a = question_four_output_a + space + str(compute_remainder(10, 3))
    return question_four_output_a

# }}}

# Question 4b. {{{

# Instructions:
# Implement the following function so that it provides all
# of the features in the function description

# Function description:
# The function is_factor should:
# --> Intuitively, answer the question "is the value of input_one a factor of input_two"?
# --> Or, ask the question as "does the value of input_one evenly divide input_two with a remainder of 0?"
# --> It must accept as input two int values called input_one and input_two
# --> It must determine whether or not input_two is evenly divided by input_one, which would
#     then mean that it should return True to indicate that input_one is a factor of input_two
# --> For instance, if input_two is equal to 10 and input_one is
#     equal to 5 then this function would return True
# --> Alternatively, if value_one is equal to 3 and value_two is
#     equal to 10 then this function would return False


def is_factor(input_one: int, input_two: int) -> bool:
    """Determine whether or not input variable a is a factor of input variable b."""
    return True


def question_four_b():
    """Run question four-b."""
    # Do not edit this function
    space = " "
    question_four_output_b = str(is_factor(2, 10))
    question_four_output_b = question_four_output_b + space + str(is_factor(3, 9))
    question_four_output_b = question_four_output_b + space + str(is_factor(3, 10))
    return question_four_output_b

# }}}

# Question 4c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function compute_ratios should:
# --> Accept as input two list of int values
# --> Divide the number in the i-th index of the first list by
#     the i-th number in the second list, producing a resulting value
# --> Store the resulting value into a list and return the final list
#     that contains the results of all of the divisions,
#     taking care to ensure that a division by zero results in the
#     storage of a not-a-number value instead of
#     the program crashing with an exception
# --> For instance, if the function receives as input these lists:
#     [1, 2, 7, 6] and [1, 2, 0, 3]
#     it will produce as output the following list:
#     [1.0, 1.0, nan, 2.0]
#     where the 'nan' designates that it is an undefined value
#     or a not-a-number


def compute_ratios(list_one: List, list_two: List) -> List[float]:
    """Compute the ratios between the numbers in the first list and the second list."""
    ratios = []
    return ratios


def question_four_c():
    """Run question four-c."""
    # Do not edit this function
    separator = " / "
    question_four_output_c = str(compute_ratios([1, 2, 7, 6], [1, 2, 0, 3]))
    question_four_output_c = question_four_output_c + separator + str(compute_ratios([], []))
    question_four_output_c = question_four_output_c + separator + str(compute_ratios([10], [0]))
    return question_four_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_four():
    """Run all of the subquestions in question four."""
    # call the function for question four-a
    output = question_four_a()
    print(output)
    # call the function for question four-b
    output = question_four_b()
    print(output)
    # call the function for question four-c
    output = question_four_c()
    print(output)


if __name__ == "__main__":
    run_question_four()
