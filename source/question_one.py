"""Question one for an executable examination."""

from typing import Tuple


# Question 1a. {{{

# Instructions:
# Implement the following function to adhere to this description

# Function description:
# The function determine_even_odd should:
# For the first output value:
# --> Return "even" (of type string) when the input variable (of type int)
#     contains an even number as its value
# --> Return "odd" (of type string) when the input variable (of type int)
#     contains an odd number as its value
# For the second output value:
# --> Return the input number that was provided as an int

# For instance, if the input number to def determine_even_odd was 10
# then the output would be: ("even", 10)
# where the output values are stored in a tuple with
# the first value stored in a string and the second stored in an int


def determine_even_odd(value: int) -> Tuple[str, int]:
    """Determine if a number is even or odd."""
    return ("", 0)


def question_one_a():
    """Run question one-a."""
    # Do not edit this function
    separator = " / "
    question_one_output_a = str(determine_even_odd(10))
    question_one_output_a = question_one_output_a + separator + str(determine_even_odd(11))
    question_one_output_a = question_one_output_a + separator + str(determine_even_odd(-11))
    question_one_output_a = question_one_output_a + separator + str(determine_even_odd(0))
    return question_one_output_a

# }}}

# Question 1b. {{{

# Instructions:
# Implement the following function to adhere to this description

# Function description:
# The function compute_square_while should:
# --> Accept as input a variable called value of type int
# --> Produce as output an int that is the square of the input value
# --> For instance, an input of 5 would produce the output of 25
# --> The function must use a while loop to perform the computation
# --> Note that it is not acceptable for the compute_square function
#     to use the built-in multiplication operator in Python
# For instance, if the function received the input of 10 it would
# return the output of 100, which is the value of 10 squared.


def compute_square_while(value: int) -> int:
    """Square the square of a number through iteration with a while loop."""
    return 0


def question_one_b():
    """Run question one-b."""
    # Do not edit this function
    space = " "
    question_one_output_b = str(compute_square_while(10))
    question_one_output_b = question_one_output_b + space + str(compute_square_while(-10))
    question_one_output_b = question_one_output_b + space + str(compute_square_while(0))
    return question_one_output_b

# }}}

# Question 1c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function compute_factorial_iterative_while should:
# --> Accept as input an int value called input_number
# --> Produce as output an int that is the input_number!
#     where the "!" designates the factorial operation
# --> For instance, if the function receives 5 as input
#     it will return the int value of 120 as output.


def compute_factorial_iterative_while(input_number: int) -> int:
    """Compute the factorial number of the provided input number with a while loop."""
    return 0


def question_one_c():
    """Run question one-c."""
    # Do not edit this function
    space = " "
    question_one_output_c = str(compute_factorial_iterative_while(5))
    question_one_output_c = question_one_output_c + space + str(compute_factorial_iterative_while(6))
    question_one_output_c = question_one_output_c + space + str(compute_factorial_iterative_while(7))
    return question_one_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_one():
    """Run all of the subquestions in question one."""
    # call the function for question one-a
    output = question_one_a()
    print(output)
    # call the function for question one-b
    output = question_one_b()
    print(output)
    # call the function for question one-c
    output = question_one_c()
    print(output)


if __name__ == "__main__":
    run_question_one()
