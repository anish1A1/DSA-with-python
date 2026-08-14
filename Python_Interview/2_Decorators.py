
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


# With 