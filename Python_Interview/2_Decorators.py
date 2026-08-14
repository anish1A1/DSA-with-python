
# Decorator are essentially a python function that add functionality to existing function in Python withouut changing the structure of the function itself.
# It wraps the function inside it.
# Represented by @decorator_name

def lowercase_decorator(func):
    def wrapper():
        result = func()
        lower_case = result.lower()
        return lower_case
    return wrapper

def splitter_decorator(func):
    def wrapper():
        result = func()
        splitter = result.split()
        return splitter
    return wrapper

@splitter_decorator    #it will work 2nd
@lowercase_decorator    #It will work first
def hello():
    return "Hello World"

print(hello())


# With arguments

def names_decorator(func):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_capitalize = func(arg1, arg2)    
        
        return string_capitalize
    return wrapper

@names_decorator
def say_hello(name1, name2):
    return "Hello " + name1 + "!, Hello " + name2 

retun_hello = say_hello('Sara', "Ansh")
print(retun_hello)

print('\n')
# With *args and **kwargs in Decorator

# Creating a logger decorator with show what is running and and the function names being runned.

import functools

def logger_decorator(func):
    
    # Best practice: preserves function metadata
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        print(f"Executing function ${func.__name__} with args: {args} and kwargs: {kwargs}")
       
        # Forward everything to the original function
        result = func(*args, **kwargs)
        print(f"${func.__name__} finished execution.")
        
        return result
    return wrapper
# Always try to use functools.wraps it keeps the metadata of the function so, that it will not return None when asked about what this function does.

@logger_decorator
def greet(name, message="Hello"):
    return f"{message}, {name}"

@logger_decorator
def add_number(a,b,c,d):
    return a+b+c+d

@logger_decorator
def multiple_number(*args):
    result = 1  
     # Initialize result to 1 because we are multiplying
     
    for i in args:
        result *= i
    return result
    
    
    
print(greet("Anish", "Nihau"))
print("\n")
print(add_number(1,3,4,56))
print('\n')
print(multiple_number(2,2,3,5,70,3,1,90,923))
# *args catches extra positional arguments as a tuple
# **kwargs catches extra keyword arguments as a dictionary