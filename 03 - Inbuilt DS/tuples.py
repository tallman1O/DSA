# Tuples are ordered collections of items that are immutable.
# They are similar to lists, but their immutability makes them different.


## Creating a tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

tpl = tuple()
print(type(tpl))

numbers = tuple([1,2,3,4,5,5])
print(numbers)

mixed_tuple = (1, "mixed", 5.9)
print(mixed_tuple)


## Accessing Tuple Elements
print(numbers[0])
print(numbers[-1]) # Indexing, Slicing similar to a list, just return type will be tuple

## Tuple Operations

concat_tuple = numbers + mixed_tuple
print(concat_tuple)

print(mixed_tuple * 3)


## Immutatble Nature of Tuples - Elements cannot be changed once assigned

lst = [1,2,3,4,5,5]
print(lst)
lst[3] = 68
print(lst)

tpl = (1,2,3,4,5,5,"rate")
print(tpl)
# tpl[4] = "new" - throw an error


## Tuple Methods
print(tpl.count(5))
print(numbers.index(3))


## Packing and Unpacking Tuple

packed_tuple = 1, "Hello", 3.14
print(packed_tuple)

#Unpacking a tuple
a,b,c = packed_tuple
print(a)
print(b)
print(c)

## Unpacking with *
numbers = (1,2,3,4,5,6,7)
first,*middle,last = numbers
print(first) # 1
print(middle) # [2,3,4,5,6]
print(last) # 7


## Nested Tuple
nested_tuple = ((1,2,3), ("a", "b", "c"), (True, False))
print(nested_tuple[0]) # (1,2,3)
print(nested_tuple[1][2]) # c

# Iterating over nested tuples

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end= " ")
    print()





