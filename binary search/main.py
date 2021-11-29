import math

sorted_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
first_num_ind = 0
last_num_ind = (len(sorted_arr) - 1)
our_target = int(input())


def binary_search(arr, start, end, target):
    if start > end:
        return False

    mid_index = math.floor((start + end)/2)
    if target == arr[mid_index]:
        return True
    if target > arr[mid_index]:
        return binary_search(arr, mid_index + 1, end, target)
    elif target < arr[mid_index]:
        return binary_search(arr, start, mid_index - 1, target)


print(binary_search(sorted_arr, first_num_ind, last_num_ind, our_target))
