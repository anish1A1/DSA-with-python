# Write a program to swap two numbers using a third variable

def swap(a, b):
    c = a
    a = b
    b = c
    print(a,b)

swap(2,6)


def SwapWithOutThirdVar(a, b):
    
    
    a,b = b, a
    print(a, b)

SwapWithOutThirdVar(7, 6)