def merge_sort(arr):
    if len(arr) > 1:
        lef_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursion
        merge_sort(lef_arr)
        merge_sort(right_arr)

        # merge
        left_ind = 0
        right_ind = 0
        merge_ind = 0
        while left_ind < len(lef_arr) and right_ind < len(right_arr):
            if lef_arr[left_ind] < right_arr[right_ind]:
                arr[merge_ind] = lef_arr[left_ind]
                left_ind += 1
            else:
                arr[merge_ind] = right_arr[right_ind]
                right_ind += 1

            merge_ind += 1

        while left_ind < len(lef_arr):
            arr[merge_ind] = lef_arr[left_ind]
            left_ind += 1
            merge_ind += 1

        while right_ind < len(right_arr):
            arr[merge_ind] = right_arr[right_ind]
            right_ind += 1
            merge_ind += 1


test_array = [2, 4, 6, 3, 7, 1]
merge_sort(test_array)
print(test_array)
