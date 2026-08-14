
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

hel = hello()
print(hel)