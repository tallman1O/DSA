def sum_of_elements(arr):
    sum = 0

    for i in arr:
        sum = sum + i

    return sum


if __name__ == "__main__":
    arr = [-1, -2, -3, -4]
    print(sum_of_elements(arr))