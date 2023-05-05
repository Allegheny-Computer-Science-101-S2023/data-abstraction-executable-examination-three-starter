"""Question two for an executable examination."""

from typing import Any

# Question 2a. {{{

# Instructions:
# Repair the source code lines in this function
# so that it operates in the specified fashion

# Function description:
# The function compute_square_for should:
# --> Compute the square of a number using a for loop
# --> For instance,
#     -- the input of 5 should return the output of 25
#     -- the input of -5 should return the output of 25
#     -- the input of 0 should return the output of 0
# Note that it is not acceptable for this function to
# use any of the built-in functions that Python provides for
# computing the square through multiplication or exponentiation


def compute_square_for(value: int) -> int:
    """Square a number through iteration."""
    answer = 0
    for _ in range(value):
        answer = value
    return answer


def question_two_a():
    """Run question two-a."""
    # Do not edit this function
    space = " "
    question_two_output_a = str(compute_square_for(10))
    question_two_output_a = question_two_output_a + space + str(compute_square_for(-10))
    question_two_output_a = question_two_output_a + space + str(compute_square_for(0))
    return question_two_output_a


# }}}

# Question 2b. {{{

# Instructions:
# Implement the following function so that it fulfills its description

# Function description:
# The function called add_digits should:
# --> Accept as input a string that only contains numerical integer digits in it
# --> Iterate through each of the single digits and convert it to an int value
# --> Compute the running total of all the int values extracted from the string
# --> Return the computed running total as an int value
# --> For instance, an input of "123" would produce the output of 6

# Note that this function should use a for loop or a while loop
# to perform the computation


def add_digits(digits: str) -> int:
    """Sum together the numerical digits in the digits string and return it as an int."""
    return 0


def question_two_b():
    """Run question two-b."""
    # Do not edit this function
    space = " "
    question_two_output_b = str(add_digits("123"))
    question_two_output_b = question_two_output_b + space + str(add_digits("321"))
    question_two_output_b = question_two_output_b + space + str(add_digits("001"))
    question_two_output_b = question_two_output_b + space + str(add_digits("301"))
    question_two_output_b = question_two_output_b + space + str(add_digits("333"))
    return question_two_output_b

# }}}

# Question 2c. {{{

# Instructions:
# Implement functions to produce the requested output

# Function description:
# The function convert_to_str should:
# --> Accept as input a value of any data type
# --> Convert the value to the type of string (i.e., it will be a str)
# --> Return the converted value, again ensuring that it is of type str
# --> For instance, if the function receives 5 as
#     an input it returns the value of "5"

# Function description:
# The function determine_if_str should:
# --> Accept as input a value of any data type
# --> Determine whether or not the provided value is a string
# --> If the value is a string, it should return True
# --> Otherwise, it should return False
# --> For instance, if the function receives 5 as
#     an input it returns False
# --> For instance, if the function receives "5" as
#     an input it returns True


def convert_to_str(value: Any) -> str:
    """Convert the provided value to a string."""
    return ""


def determine_if_str(value) -> bool:
    """Determine whether or not a provided value is a string."""
    return False


def question_two_c():
    """Run question two-c."""
    # Do not edit this function
    space = " "
    question_two_output_c = str(determine_if_str(5))
    question_two_output_c = question_two_output_c + space + str(determine_if_str(convert_to_str(5)))
    question_two_output_c = question_two_output_c + space + str(determine_if_str(convert_to_str(5.5)))
    return question_two_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_two():
    """Run all of the subquestions in question two."""
    # call the function for question two-a
    output = question_two_a()
    print(output)
    # call the function for question two-b
    output = question_two_b()
    print(output)
    # call the function for question two-c
    output = question_two_c()
    print(output)


if __name__ == "__main__":
    run_question_two()
