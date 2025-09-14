def sum_of_array(arr):
    n = len(arr)

    if n == 0:
        return 0

    sumOfRemainingArray = sum_of_array(arr[1:])

    ans = arr[0] + sumOfRemainingArray

    return ans


print(sum_of_array([2,3,4]))