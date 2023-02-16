def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


print(sum_array([6, 7, 8, 19, 10]))
