def maximum_element(arr):
    max_num = arr[0]

    for i in arr:
        if i > max_num:
            max_num = i

    return max_num

if __name__ == "__main__":
    print(maximum_element([-10, -5, -20]))