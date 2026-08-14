
# Every object has its own scope in python, whereever, they are initializer they will work in that scope only.

temp = 10
def func():
    temp = 20
    print(temp)
print(temp)
func()
print(temp)

# Here since, temp of func() has its own scope and when the funtion gets cleared its scope also gets cleared out. so temp is 20 only inside function.

print('\n')
# But to make the scope of temp to work and be used outside the function. Use global keyword.

temp = 10 
def func():
    global temp
    temp = 20
    print(temp)
print(temp)
func()
print(temp)