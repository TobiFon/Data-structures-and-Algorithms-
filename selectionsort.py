def selection_sort(list):
    for i in range(len(list) - 1):
        lowest_number_index = i

        for j in range(lowest_number_index + 1, len(list)):
            if list[j] < list[lowest_number_index]:
                lowest_number_index = j

        if (lowest_number_index != i):
            temp = list[i]
            list[i] = list[lowest_number_index]
            list[lowest_number_index] = temp

    return list


print(selection_sort([333, 17, 753, 80, 202]))
