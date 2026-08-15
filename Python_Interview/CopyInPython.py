
list1 = [1,2,3]
list2 = list1

list2.append(4)
print(f"List 1 is {list1}")
print(f"List 2 is {list2}")

# Here if i change the list2 the list1 will also change.
#  The " = " operator does not copy the object
# It creates a new reference to the exact same memory location.

# When we created list1 it had its own memory address, but when we added list2 inititalizing it as list1
# list2 created a new reference to the memory address of list1

# to fix this we can use copy.copy() for shallow copy and copy.deepcopy() for deep copy

import copy

list1 = [1,2,3]
list2 = copy.copy(list1)

list2.append(4)

print(f"List 1 is {list1}")
print(f"List 2 is {list2}")

# The copy.copy() will create a new array while sharing the same references
# Here list2 got populated with the same reference of list1 
# But one problem, nested array will not work with shallow copy,

list3 = [[1,2], [3,4]]
list4 = copy.copy(list3)

list4[0][0] = 99 

# Since it is a shallow copy, changing nested object will change also change original array.

print(f"List 3 is {list3}")
print(f"List 4 is {list4}")
