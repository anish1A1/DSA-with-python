
x = [i for i in range(5)]
print(x)

x = {i: i**2 for i in range(5)}
print(x)


mul = lambda x, y : x*y
print(mul(2,4))

# Using lambda inside a function
def myWrapper(n):
    return lambda a: a*n

muls = myWrapper(10)
print(muls(5))