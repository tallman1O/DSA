def move_zeroes(arr):
    n = len(arr)
    end = n - 1
    pos = 0

    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    while pos < n:
        arr[pos] = 0
        pos += 1



    return arr

if __name__ == "__main__":
    arr = [1,2,0,5,0,3,4,5]
    print(move_zeroes(arr))