def missing_num(arr):
    n = len(arr)
    sum_of_array = sum(arr)
    expected_sum = n * (n + 1) // 2

    missing = expected_sum - sum_of_array
    return missing

if __name__ == '__main__':
    arr = [3, 0, 1]
    print(missing_num(arr))