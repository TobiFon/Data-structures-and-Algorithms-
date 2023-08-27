def insertion_sort(array):
    for i in range(1, len(array)):

        temp = array[i]
        position = i - 1

        while position >= 0:
            if array[position] > temp:
                array[position + 1] = array[position]
                position = position - 1

            else:
                break

        array[position + 1] = temp
    return array


print(insertion_sort([80, 3, 17, 202, 75]))
