"""
Python is a Case sensitive Language
"""
name = "MEHUL"
Name = "mehul"

print(name) ## MEHUL
print(Name) ## mehul

'''
2. Identation :
Indentation in Python is used to define the structure and hierarchy of the code. 
Unlike many other programming languages that use braces {} to delimit blocks of code, 
Python uses indentation to determine the grouping of statements. 
This means that all the statements within a block must be indented at the same level.
'''

age = 32
if age > 45:
    age = 45
    print(age)

print(age)

'''
Line Continuation
'''

total = 1+2+3+4+5+6+\
        4+10

print(total)

'''
Multiple Statements on a single line
'''

x=5;y=10;z=x+y
print(z)


'''
Semantics - Type of variables
'''
name = "mehul"
age = 24

print(type(name))
print(type(age))

'''
Dynamic Typing - Python allows the type of the variables to be determined at runtime.
'''

age = '25'
print(age)
print(type(age))

## Type Conversion
new_age = int(age)
print(type(new_age))

'''
Input
'''

wt = input("Enter your weight: ")
print(wt)
print(type(wt))

new_wt = int(input("Enter your weight new: "))
print(type(new_wt))