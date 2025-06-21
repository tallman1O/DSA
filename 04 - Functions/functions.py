## A function is a block of code that performs specific task. Functions Help in organizing code, reusing code, and improving readilbilty.

## Syntax
def function_name(paramteres):
    """DocString - to explainn what the function does"""
    #Function Body
    return expression

def check_even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = 22
check_even_or_odd(number)


## Default parameters
def greet(name = "Mehul"):
    print(f"Hello {name}")

greet() # Hello Mehul


## Variable Length Arguments
## Positional and Keywords Arguments

# Positional Arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5,5,6) #1,2,3,4,5,6 - are positional arguments

# Keywords Arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krish", age=32, country="India")


## Return Statements
def multiply(a,b):
    return a*b

product = multiply(2,3)
print(product)
