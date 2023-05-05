"""Question seven for an executable examination."""

from typing import Dict
from typing import List
from typing import Tuple


# Question 7a. {{{

# Instructions:
# Fix any defect(s) in the methods of the Person class so that the
# create_person_objects function produces the correct output

# Instructions:
# Implement the following function so that it fulfills its description

# Function description:
# The function create_person_objects should:
# --> Accept as input an integer value called person_count that describes the
#     number of identical people who should be added to the list
# --> Using the default values provided below, this functions should create
#     the number of people objects specified by the person_count variable
#     and store them in a list
# --> Finally, it should return the list so that its values can be displayed
#     through the use of the provided __repr__ function

# The person that you create should always have these default attribute values:
# Name: "Timothy James"
# Country: "the United States of America"
# Telephone Number: "1-814-573-1299"
# Job: "Systems Administrator"
# Email: "james@gmail.com"

# If the function was provided with the input value of 0 for person_count it would
# produce an empty list represented as []

# If the function was provided with the input value of 1 for person_count it would
# produce the following list containing a single person object's textual representation:

# [Timothy James is a Systems Administrator who lives in the United States of
# America and can be contacted at 1-814-573-1299 or james@gmail.com]

# Note that the information about a Person should always be displayed so that the telephone
# number comees before the email address in the contact information


class Person:
    """Define a Person class."""

    def __init__(
        self, name: str, country: str, phone_number: str, job: str, email: str
    ) -> None:
        """Define the constructor for a person."""
        self.name = name
        self.country = country
        self.phone_number = phone_number
        self.job = job
        self.email = email

    def __repr__(self) -> str:
        """Return a textual representation of the person."""
        return f"{self.name} is a {self.country} who lives in {self.job} and can be contacted at {self.email} or {self.phone_number}"


def create_person_objects(person_count: int) -> List[Person]:
    """Create the specifiied number of person objects using default values."""
    person_list = []
    return person_list


def question_seven_a():
    """Run question seven-a."""
    # Do not edit this function
    separator = " / "
    question_seven_a = str(len(create_person_objects(3))) + " = " + str(create_person_objects(3))
    question_seven_a = question_seven_a + separator + str(len(create_person_objects(0))) + " = " + str(create_person_objects(0))
    return question_seven_a

# }}}

# Question 7b. {{{

# Instructions:
# Implement a function that performs the following operation

# Function description:
# The function convert_list_to_paired_dictionary should:
# --> Accept as input a variable called input_list that is a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a dictionary (i.e., a dict) that maps the string value to the int value
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output {'5': 5, '7': 7, '9': 9, '11': 11}


def convert_list_to_paired_dictionary(input_list: List[str]) -> Dict[str, int]:
    """Convert a list of strings to a dictionary that maps the strings to their int values."""
    output_dict_for_pairing: Dict[str, int] = {}
    return output_dict_for_pairing


def question_seven_b():
    """Run question seven-b."""
    # Do not edit this function
    separator = " / "
    question_seven_output_b = str(convert_list_to_paired_dictionary(['5', '7', '9', '11']))
    question_seven_output_b = question_seven_output_b + separator + str(convert_list_to_paired_dictionary(['1', '2', '3', '4']))
    return question_seven_output_b

# }}}

# Question 7c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function sum_list should:
# --> Accept as input a tuple of four int values
# --> Compute the sum of all of the int values in the tuple
# --> Return the sum of all the int values in the tuple
# --> For instance, if the function receives (5, 7, 9, 11) as
#     an input it returns the dictionary that contains {(5, 7, 9, 11): 32}
# Note that this function is not required to handle any other inputs than
# a tuple that contains four int values


def sum_list(input_list: Tuple[int, int, int, int]) -> Dict[Tuple[int, ...], int]:
    """Sum all of the values inside of a list of int values."""
    input_list_sum = 0
    return input_list_sum


def question_seven_c():
    """Run question seven-c."""
    # Do not edit this function
    separator = " / "
    question_seven_output_c = str(sum_list((int(5), int(7), int(9), int(11))))
    question_seven_output_c = question_seven_output_c + separator + str(sum_list((int(1), int(2), int(3), int(4))))
    return question_seven_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_seven():
    """Run all of the subquestions in question seven."""
    # call the function for question seven-a
    output = question_seven_a()
    print(output)
    # call the function for question seven-b
    output = question_seven_b()
    print(output)
    # call the function for question seven-c
    output = question_seven_c()
    print(output)


if __name__ == "__main__":
    run_question_seven()
