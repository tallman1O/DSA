def sum_of_array(arr):
    n = len(arr)

    if n == 0:
        return 0

    return arr[n - 1] + sum_of_array(arr[:n - 1])


print(sum_of_array([2,3,4]))