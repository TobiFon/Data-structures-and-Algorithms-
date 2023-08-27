import math


def binary_search(array, value):

    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:

        midpoint = math.floor((lower_bound + upper_bound)/2)

        midpoint_value = array[midpoint]

        if value == midpoint_value:
            return midpoint

        elif value < midpoint_value:
            upper_bound = midpoint - 1

        elif value > midpoint_value:
            lower_bound = midpoint + 1


print(binary_search([3, 17, 75, 80, 202], 80))
