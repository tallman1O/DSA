def reverse_array(arr):
    # return arr[::-1]

    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

if __name__ == "__main__":
    arr = [-1, -2, -3, -4]
    print(reverse_array(arr))