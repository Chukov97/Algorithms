def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        elem = arr[0]
        left = [i for i in arr[1:] if i < elem]
        right = [i for i in arr[1:] if i >= elem]
        return quicksort(left) + [elem] + quicksort(right)


print(quicksort([10, 4, 4, 2, 3, 7]))
