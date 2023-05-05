"""Question nine for an executable examination."""

from typing import Dict
from typing import List
from typing import Tuple

# Question 9a. {{{

# Instructions:
# Implement the following function so that it:
# --> Creates a dictionary called dog_name_to_age_dictionary
#     that stores the name of a Dog and then the age of the dog.
# --> It must store information about these three dogs:
#     Bosco is a dog that is eight years old
#     Miles is a dog that is two years old
#     Sophie is a dog that is nine years old
# --> It must then perform dictionary lookups so that
#     it correctly looks up the ages of the dogs and stores them in
#     a list of int values, ultimately producing [8, 2, 9]
# --> Finally, it should return the entire dictionary and
#     the list that contains the dog ages in a containing tuple

# Ultimately, when this function is called it should produce this output:
#
# ({'Bosco': 8, 'Miles': 2, 'Sophie': 9}, [8, 2, 9])

# Note that this function cannot be hard-coded to produce
# the output {'Bosco': 8, 'Miles': 2, 'Sophie': 9}. It
# must create the dictionary that contains these key-value
# pairs through any viable approach to creating a dictionary
# (i.e., a dict in Python) and then adding the content to it

# Note that this function cannot be hard-coded to produce
# the output [8, 2, 9]. It must create the dictionary and
# then perform the lookups so that it demonstrates your
# understanding of how to create and search in a dictionary.
# When the Python source code performs the lookups, it
# should make sure to lookup the names when they are
# surrounded by double quotation marks.

# Note that in this output example the parentheses designate the
# start and end of a tuple, the curly braces designate the start
# and end of a dictionary, and the brackets designate the start
# and end of a list.

# Note that the name of the dictionary must be dog_name_to_age_dictionary!

# Finally, remember, the output must precisely match the above format!


def create_dictionary_and_search_for_value() -> Tuple[Dict[str, int], List[int]]:
    """Construct a dictionary of int values and then search for specific values."""
    dog_name_to_age_dictionary = {}
    return dog_name_to_age_dictionary


def question_nine_a():
    """Run question nine-a."""
    # Do not edit this function
    question_nine_output_a = str(create_dictionary_and_search_for_value())
    return question_nine_output_a

# }}}

# Question 9b. {{{

# Instructions:
# Implement this function so that it operates in the specified fashion

# Function description:
# The function calculate_powers_while_loop should:
# --> Accept as input a minimum and a maximum value for computing 2 to the power
#     of a specific number between the inclusive minimum and the exclusive maximum
# --> Store all of the values that result from performing the exponentiation in a list
#     and return them to the calling function
# --> For instance, when the function has the following inputs it will produce the stated outputs
#     Input: 2 for the minimum and 5 for the maximum
#     Output: [4, 8, 16]
# --> Note that this function must perform the computation using a while loop


def calculate_powers_while_loop(base: int, minimum: int, maximum: int) -> List[int]:
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum for the specified base."""
    powers_list = []
    return powers_list


def question_nine_b():
    """Run question nine-b."""
    # Do not edit this function
    separator = " / "
    question_nine_output_b = str(calculate_powers_while_loop(2, 1, 5))
    question_nine_output_b = question_nine_output_b + separator + str(calculate_powers_while_loop(2, 1, 10))
    question_nine_output_b = question_nine_output_b + separator + str(calculate_powers_while_loop(2, 4, 5))
    return question_nine_output_b

# }}}

# Question 9c. {{{

# Instructions:
# Fix the defect(s) in the greedy_knapsack_solver function so that
# it can correctly solve an instance of the 0/1 knapsack problem
# through the use of three different greedy heuristics

# Please note that there are several regions of code where there
# __is not__ a defect. You do not need to edit any of the functions
# inside of these designated regions.

# The correct implementation of the greedy_knapsack_solver function
# should ensure that greedy knapsack solving with these heuristics:
#
# 1) Greedy by weight
# 2) Greedy by value
# 3) Greedy by density
#
# ... always pick the correct elements and always ensure that they do
# so in a fashion that follows their heuristic and does not
# violate the constraint that the final sum of the weight of the
# elements does not go over the stated maximum weight of the knapsack

# Every aspect of the output from running each of three three solvers
# must match precisely the output format. Importantly, if you modify
# any of the source code that produces the output (that was marked
# as not containing the defect) and then the program does not work
# correctly you are responsible for repairing the provided code.

# None of the functions between these curly brackets have defects {{{


class Item(object):
    """Define an item used to represent an element in a knapsack problem instance."""

    def __init__(self, n, v, w):
        """Construct an instance of the Item class."""
        self._name = n
        self._value = v
        self._weight = w

    def get_name(self) -> str:
        """Access the name of an Item."""
        return self._name

    def get_value(self) -> int:
        """Access the value of an Item."""
        return self._value

    def get_weight(self) -> int:
        """Access the weight of an Item."""
        return self._weight

    def __repr__(self) -> str:
        """Produce a textual representation of the Item."""
        return f"({self._name}, {self._value}, {self._weight})"


def value(item: Item) -> int:
    """Return the value for a specific item."""
    return item.get_value()


def weight_inverse(item: Item) -> float:
    """Return the inverse of the weight for a specific item."""
    return 1.0 / item.get_weight()


def density(item: Item) -> float:
    """Return the density of the item."""
    return item.get_value() / item.get_weight()

# }}}

# Note: investigate the greedy_knapsack_solver function for defects {{{


def greedy_knapsack_solver(items: List[Item], max_weight: int, key_function) -> Tuple[List[Item], float, float]:
    """Perform the greedy algorithm for items, a maximum weight of a knapsack, and an objective function."""
    items_copy = sorted(items, key=key_function, reverse=True)
    result: List[Item] = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight()) < max_weight:
            result.append(items_copy[i])
            total_weight = items_copy[i].get_weight()
            total_value = items_copy[i].get_value()
    return (result, total_weight, total_value)

# }}}

# None of the functions between these curly brackets have defects {{{


def build_items() -> List[Item]:
    """Create an instance of a 0/1 knapsack using instances of the Item class."""
    names = ["Clock", "Painting", "Radio", "Vase", "Book", "Computer"]
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items: List[Item] = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items


def run_greedy_solver_for_key_function(items: List[Item], max_weight: int, key_function) -> str:
    """Run the greedy algorithm and display the result."""
    taken, value, weight = greedy_knapsack_solver(items, max_weight, key_function)
    running_output = f", total item value: {value}, total item weight: {weight}, item(s):"
    for item in taken:
        running_output = f"{running_output} {item}"
    return running_output


def run_all_greedy_knapsack_solvers(max_weight=20) -> str:
    """Run all greedy algorithm with all possible objective functions."""
    items = build_items()
    separator = "/"
    running_output = ""
    running_output = f"{running_output}Knapsack size: {max_weight}"
    running_output = f"{running_output}, Greedy-by-value"
    running_output = f"{running_output}{run_greedy_solver_for_key_function(items, max_weight, value)} {separator} "
    running_output = f"{running_output}Greedy-by-weight"
    running_output = f"{running_output}{run_greedy_solver_for_key_function(items, max_weight, weight_inverse)} {separator} "
    running_output = f"{running_output}Greedy-by-density"
    running_output = f"{running_output}{run_greedy_solver_for_key_function(items, max_weight, density)}"
    return running_output

# }}}


def question_nine_c():
    """Run question nine-c."""
    # Do not edit this function
    question_nine_output_c = run_all_greedy_knapsack_solvers()
    return question_nine_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_nine():
    """Run all of the subquestions in question nine."""
    # call the function for question nine-a
    output = question_nine_a()
    print(output)
    # call the function for question nine-b
    output = question_nine_b()
    print(output)
    # call the function for question nine-c
    output = question_nine_c()
    print(output)


if __name__ == "__main__":
    run_question_nine()
