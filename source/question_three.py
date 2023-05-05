"""Question three for an executable examination."""

from pathlib import Path
from typing import List

# Question 3a. {{{

# Instructions:
# Implement the source code lines in this function
# so that it operates in the specified fashion

# Function description:
# The function input_file should:
# --> Accept as input a file_name that is of type string
# --> Assume that the program that runs the function will
#     be executed from the root of the GitHub repository;
#     as in "python source/question_three.py"
# --> Construct a pathlib Path object and then read in the
#     values from the file and store them as strings in a list
# --> Return a list of strings containing all of the values
#     that were stored inside of the file.
# --> For instance, the inputs/observations.txt file contains these values:
#     5
#     7
#     9
#     11
#
#     This means that it would cause this function to produce the output:
#     ['5', '7', '9', '11']

# Please remember that this function should create an instance of the Path
# class provided by the pathlib package to read in the file!


def input_file(file_name: str) -> List[str]:
    """Use a pathlib Path object to read and return the contents of the specified file."""
    return [""]


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    question_three_output_a = input_file("inputs/observations.txt")
    return question_three_output_a

# }}}

# Question 3b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function binary_search_list should:
# --> Accept as input a variable called input_list that contains a list of ints
# --> Use an iterative binary search to find the value and return it or,
#     alternatively, conclude that the value cannot be found and return -1
# --> For instance, when the function receives the inputs:
#     Input List: [5, 7, 9, 11]
#     Search Value: 9
#     ... it would return the following value: 2

# Please note that you should use the comments inside of the binary_search_list
# function to better understand the purpose of the source code as you are
# finding and fixing the defects in this function


def binary_search_list(input_list: List[int], search_value: int) -> int:
    """Use a binary search technique to find a specific value in a list."""
    # initialize the starting configuration for the search
    low = 0
    high = len(input_list) - 1
    mid = 0
    # iteratively search through the list of values
    while low <= high:
        mid = (high + low) // 2
        # if x is greater, ignore left half
        if input_list[mid] > search_value:
            low = mid + 1
        # if x is smaller, ignore right half
        elif input_list[mid] < search_value:
            high = mid - 1
        # this means that x is present at mid-point value
        else:
            return mid - 1
    # if we reach this line, then the element was not present
    # so the function returns negative one to indicate
    # that the search failed and the value was not found
    return -1


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    separator = " / "
    question_three_output_b = str(binary_search_list([5, 7, 9, 11], 9))
    question_three_output_b = question_three_output_b + separator + str(binary_search_list([5, 7, 9, 11], 99))
    question_three_output_b = question_three_output_b + separator + str(binary_search_list([5, 7, 9, 11], -9))
    question_three_output_b = question_three_output_b + separator + str(binary_search_list([5, 7, 9, 11], 11))
    return question_three_output_b

# }}}

# Question 3c. {{{

# Instructions:
# Correct the defect(s) in this function so that it produces the requested output

# Function description:
# The function bubble_sort should:
# --> Accept an input list of int values as input and produce a sorted list
#     of values such that the list is in ascending order

# To correctly implement this function you need to know the definition
# of the following algorithms and concepts:
# --> sorting algorithm
# --> bubble sorting algorithm
# --> ascending order for a list of data

# Please note that this function only needs to work for lists of int values


def bubble_sort(array: List[int]) -> List[int]:
    """Sort an input list called array using bubble sort."""
    n = len(array)
    for i in range(n):
        # create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True
        # start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been sorted.
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                # if the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j + 1], array[j] = array[j], array[j + 1]
                # since you had to swap two elements,
                # set the already_sorted flag to False so the
                # algorithm doesn't finish prematurely
                already_sorted = False
        # if there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break
    return array


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    input_list = [56, 3, 5, 9, 0, -10, 5, 77, 9, 101]
    sorted_list = bubble_sort(input_list)
    question_three_output_c = str(sorted_list)
    return question_three_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
