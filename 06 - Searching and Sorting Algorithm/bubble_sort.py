def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == '__main__':
    arr = [120, 24, 21, 12, 11, 1, 54, 23]
    result = bubble_sort(arr)
    print(result)