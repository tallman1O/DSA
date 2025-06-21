def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (end + start) // 2  # Always use floor division instead of normal division to avoid float value
        if (arr[middle] == target):
            return middle
        elif (arr[middle] > target):
            end = middle - 1
        else:
            start = middle + 1
    return -1


if __name__ == '__main__':
    arr = [10, 23, 35, 45, 50, 70, 85]
    target = 2

    result = binary_search(arr, target)
    print("index: ",result)