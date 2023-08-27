def linear_search(array, value):
    for index, element in enumerate(array):
        if element == value:
            return index

        elif element > value:
            break
        return


print(linear_search([3, 17, 75, 80, 202], 3))
