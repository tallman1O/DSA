# filter() function constructs an iterator from elements of an iterable for which a function returns true.
# It is used to filter out items from a list(or any other iterable) based on a condition.

def even(number):
    if number % 2 == 0: return True

lst = [1,2,3,4,5,6,7,8,9]

print(list(filter(even, lst)))


## filter with a lambda function
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list(filter(lambda x: (x ** 2) % 2 == 0, numbers)))

nums = [-4, -1, 3, 6, 10]
for i in range(len(nums)):
    nums[i] = nums[i]*nums[i]
nums.sort()
print(nums)