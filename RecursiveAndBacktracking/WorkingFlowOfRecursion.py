# A Python 3 program to
# demonstrate working of
# recursion

def printfun(test):
    if (test < 1):
        return
    else:
        print(test, end = " ")
        printfun(test-1)
        print(test, end =" ")
        return
        
test = 4
print(printfun(test))