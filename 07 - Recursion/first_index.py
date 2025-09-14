# Given an array and an element, find the first index of the element in the array.

def first_index(arr, x):
    if len(arr) == 0:
        return -1

    if arr[0] == x:
        return 0

    ans = first_index(arr[1:], x)

    if ans == -1:
        return -1
    else:
        return ans + 1


def last_index(arr, x):
    if len(arr) == 0:
        return -1

    if arr[-1] == x:
        return len(arr) - 1

    ans = last_index(arr[:-1], x)

    if ans == -1:
        return -1
    else:
        return ans

print(first_index([1,2,3,4,5], 3))