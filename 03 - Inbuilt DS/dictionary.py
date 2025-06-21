# {key : value}
# Dictionaries are unordered collections of items, store data in key-value pairs.
# Keys must be unique and immutable, while values can be of any type

## Creating Dictionaries
empty_dict = {}
print(type(empty_dict))

empty_dict2 = dict()
print(empty_dict2)

student = {"name": "Mehul", "age" : 21, "grade": 68}
print(student)


## Accessing Dictionary Elements
print(student['grade'])

# using get() method
print(student.get('grade'))
print(student.get('age'))
print(student.get('last_name')) # O/P - None

# Set a default value for keys not available
print(student.get('last_name', "N/A")) # O/P - N/A


## Modifying Dictionary Elements
# Dictionary are mutable, so we can add, update or delete
print(student['age'])
student['age'] = 32 # Update the value for a key
student['address'] = "India" # Added a new key and its value
print(student)

del student['grade'] # Delete key and value pair
print(student)


## Dictionary Methods
keys = student.keys() # Get all the Keys
print(keys)

values = student.values() # Get all the values
print(values)

items = student.items() # Get all the key value pairs
print(items)


## Shallow Copy
student_copy = student
print("Student Copy: ", student_copy)
print("Student OG", student)

student['name'] = "Mehul Uttam"
print("Student Copy: ", student_copy)
print("Student OG", student)

student_copy2 = student.copy() # Shallow Copy
print("Student_copy2: ", student_copy2)


## Iterating Over Dictionaries

# Iterating over keys
for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

for key,value in student.items():
    print(key, value)


## Nested Dictionaries
students = {
    "student1": {"name": "Mehul", "age": 20},
    "student2": {"name": "Uttam", "age": 19}
}

print(students)

# Access Nested Dictionaries elements
print(students["student1"]["age"])


## Dictionary Comprehension
sq = {x: x**2 for x in range(5)}
print(sq)

## Condition Dictionary Comprehension
sq_even = {x: x**2 for x in range(10) if x%2 == 0}
print(sq_even)


## Merge 2 dictionaries into 1
dict1 = {"a": 2, "b": 3}
dict2 = {"c": 5, "d": 6}
merge_dict12 = {**dict1, **dict2}
print(merge_dict12)


## Example - Use a dictionary to count the frequency of elements in list
nums = [1,2,2,3,3,3,4,4,4,4,4,4,5,6]
frequncy = {}

for num in nums:
    if num in frequncy:
        frequncy[num]+=1
    else:
        frequncy[num]=1
print(frequncy)

