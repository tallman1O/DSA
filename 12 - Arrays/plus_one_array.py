def plus_one_array(arr):
    num = int("".join(map(str, arr)))
    sum = num + 1
    result = list(map(int, str(sum)))


    return result

if __name__ == "__main__":
    arr = [1,2,3]
    print(plus_one_array(arr))

    arr2= [9,9,9]
    print(plus_one_array(arr2))