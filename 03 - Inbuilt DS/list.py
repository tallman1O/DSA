# Lists are ordered, mutable collections items
# They can contain items of different data types

list = []
print(type(list))

names = ['mehul', 'uttam', 'savio', 45, 65, 4.2]
print(names)

#Indexing [0,1,2,3,4,5,...]
print(names[3])
print(names[-1])

#Slicing - list[start : end - 1 : step]
print(names[1:3])
print(names[1:])
print(names[:])
print(names[:-1])

#mutability
names[3] = 20
print(names)

#List Methods

names.append("orange") # Add an item to the end
print(names)

names.insert(1 ,"apple") # Add an item to a particular index
print(names)

names.remove("apple") # Removes the first occurance of that item
print(names)

names_pop = names.pop() # Remove and return the last element
print(names_pop)
print(names)

names_index = names.index("uttam")
print(names_index)

names.insert(2, "mehul")
print(names)
print(names.count("mehul")) #Counts the occurances of that item

age = [23,45,2,24,634,3,12,19]
age.sort() #Sorts the list in ascending order
print(age)

age.reverse() # sorts the list in descending order
print(age)

names.clear() # Remove all items from the list
print(names)


# Slicing lists
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[2:5])
print(nums[:5])
print(nums[5:])
print(nums[::2])
print(nums[::-1])
print(nums[::-2])


# Iterating over list
for num in nums:
    print(num)

# Iterating over list with index
for i, num in enumerate(nums):
    print(i, num)


# List comprehension
lst = []
for x in range(10):
    lst.append(x**2)
print(lst)

# Basic List Comprehension
sq = [num**3 for num in range(10)]
print(sq)

# List Comprehension with condition
even = [num for num in range(10) if num%2 == 0]
print(even)

