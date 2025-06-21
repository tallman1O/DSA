# map() - Applies a function to all items in a list

numbers = [1,2,3,4,5,6,7]
summa = map(lambda x: x**2, numbers)
print(summa)

print(list(map(lambda x: x**2, numbers)))

def square(numbers):
    return numbers**3

print(list(map(square, numbers)))


## Map Multiple Iterables
numbers1 = [1,2,3]
numbers2 = [4,5,6]

sum = list(map(lambda x,y: x+y, numbers1, numbers2))
print(sum)


## map() to convert a list of strings to integers

str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)


##
def get_name(person):
    return person['name']

people = [
    {'name': "Krish", 'age': 12},
    {'name': "Mehul", 'age': 24}
]
print(list(map(get_name, people)))