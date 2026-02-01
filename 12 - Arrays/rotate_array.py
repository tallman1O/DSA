def rotate_array(arr, k):
    n = len(arr)

    #this logic is for when k > n so as to reduce the number to times to rotate the array.
    k = k % n

    return arr[k:] + arr[:k]


if __name__ == "__main__":
    arr = [2,5,3,7,1,4,6]
    print(rotate_array(arr, 8))
