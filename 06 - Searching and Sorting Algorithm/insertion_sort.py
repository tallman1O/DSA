def insertion_sort(arr):
    n = len(arr)
    for i in range (1, n):  # i = cuurent card
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    arr = [12,25,11,34,90,22]
    print(insertion_sort(arr))
