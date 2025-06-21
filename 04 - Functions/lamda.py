# Lamda Functions are small anonymous functions are defined using the lambda keyword. They can have any number of arguments but only one expression.
# They are commonly used for short operations or as arguments to higher order functions.
# Anonymous functions are functions without a name

# Syntax
lambda arguments: expression

def add(a,b):
    return a+b;

addition = lambda c,d: c+d
print(type(addition))
print(addition(4,5))

