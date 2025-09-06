def check_sorted_array(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True

    ans = check_sorted_array(arr[1:])

    if arr[0] < arr[1]:
        return ans
    else:
        return False


# More optimized approach
def check_sorted_array2(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True

    if arr[0] < arr[1]:
        return check_sorted_array2(arr[1:])
    else:
        return False


print(check_sorted_array2([2,3,6,7,9]))
print(check_sorted_array([2,3,6,7,9]))