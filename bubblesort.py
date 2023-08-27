def bubble_sort(list):
    unsorted_until = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i + 1], list[i]
                sorted = False
                print(unsorted_until, range(unsorted_until))
        unsorted_until -= 1

    return list


print(bubble_sort([80, 3, 17, 202, 75]))
