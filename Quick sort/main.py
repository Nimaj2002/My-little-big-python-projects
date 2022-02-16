def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i] , arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quicksort(arr, left, right):
    """arr is list, left is index of first item in list, and right is the last item in list"""
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


our_list = [1, 5, 6, 2, 7, 4, 100]
quicksort(our_list, 0, len(our_list) - 1)
print(our_list)
