
def linear_search(arr, target):
    for i in range(0,len(arr)):
        if target == arr[i]:
            return i
    return -1



arr = [1,2,5,4,43,56,6,5,41,3,5,5,3,1]
target = 5

result = linear_search(arr, target)
print("index of element :", result)