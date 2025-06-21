sets = {1, 2, 3, 4, 5}
print(sets)

# Store collections of unique items. They are unordered - elements do not follow a specific order, and they do not allow duplicate items.
# Sets are useful for - membership tests, eliminating duplicates, and performing mathematical set operations.


## Create a Set
print(type(set))

test_set = {1,2,3,4,5,6,6,6,7,8,765,4,3,5}
print(test_set) # Only unique items will be printed

## Sets Operation

## 1. Adding and removing elements
my_set={4}
my_set.add(7)
print(my_set)

# 2. Removing an Element
my_set.remove(4) #item value
print(my_set)

my_set.discard(10) # It will not give an error if element is not present
print(my_set)

#pop method
removed_item = my_set.pop()
print(removed_item)

# clear all elements
my_set.clear()
print(my_set)


# Set Membership Test
my_set = {1,2,3,4,5,6,7,8}
print(3 in my_set)
print(10 in my_set)

# Mathematical Operation
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {4,5,6,7,8,9,10,2}

# 1. Union
union_set = set1.union(set2)
print(union_set)

#2. Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2) # perform intersection and update the set -> set1.
print(set1)

set1 = {1,2,3,4,5,6,7,8,9}

# 3. difference
difference_set = set1.difference(set2)
print(difference_set)


## Sets Methods

set1 = {1,2,3}
set2 = {4,5,6,3}

print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))


## list -> set
lst = [1,2,3,4,4,5,5,6,4]
list_set = set(lst)
print(list_set)

## Counting Unique Words in text

text = "In this tutorial we are discussing about sets and we are learning also about sets"

words = text.split()
print(words)

unique_words = set(words)
print(unique_words)

count_unique_words = len(unique_words)
print(count_unique_words)





