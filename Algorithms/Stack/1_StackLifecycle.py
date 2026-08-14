"""
1. What is a Stack?

A Stack is a linear data structure that follows:
LIFO — Last In, First Out

       ┌─────┐
       │  4  │ ← Last inserted
       ├─────┤
       │  3  │
       ├─────┤
       │  2  │
       ├─────┤
       │  1  │ ← First inserted
       └─────┘

append, peek, Pop  has time complexity of 0(1) 
"""

stack = []
# 1st
# We first get an empty array

# 2nd
# we add elements in the array
stack.append(9)
stack.append(15)
stack.append(5)
stack.append(11)

print(stack)

# 3rd 
# We peek the value that is going to pop out
peek = stack[-1]
print(peek)


# 4th 
# We pop the values as LIFO rule
result = stack.pop()
print(result)