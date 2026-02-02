def is_array_sorted(arr):
    # sorted_arr = sorted(arr)
    #
    # if sorted_arr == arr:
    #     return True
    # else:
    #     return False

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False

    return True


if __name__ == '__main__':
    arr = [1,2,3,6,8,7]
    print(is_array_sorted(arr))