def find_all_index(arr, x, start=0):
    if start == len(arr):
        return []

    # Check current element
    if arr[start] == x:
        return [start] + find_all_index(arr, x, start + 1)
    else:
        return find_all_index(arr, x, start + 1)


print(find_all_index([1, 2, 4, 3, 65, 75, 3, 2, 3, 5, 3], 3))