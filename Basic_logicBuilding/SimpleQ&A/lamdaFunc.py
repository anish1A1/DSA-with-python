

list1 = [2,4,5,6,722,33,53]

list1.sort(key= lambda x : x < 50)
print(list1)


"""
1. Using sorted() with lambda:
The sorted() function returns a new sorted list from an iterable without modifying the original. The key parameter accepts a function that is applied to each element before comparison.
"""
data = [('apple', 3), ('banana', 1), ('cherry', 2)]
# Sort by the second element (numerical value)
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data)
# Output: [('banana', 1), ('cherry', 2), ('apple', 3)]






"""
2. Using .sort() with lambda:
The .sort() method sorts a list in-place, modifying the original list. Similar to sorted(), it also accepts a key parameter for custom sorting.

"""

numbers = [{'value': 10}, {'value': 5}, {'value': 15}]
# Sort by the 'value' key in each dictionary
numbers.sort(key=lambda item: item['value'])
print(numbers)
# Output: [{'value': 5}, {'value': 10}, {'value': 15}]




people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
# Sort by age
people.sort(key=lambda person: person['age'])
print(people)




data = [('apple', 5), ('banana', 2), ('cherry', 8)]
# Sort by the first element (string value) of each tuple in reverse order
sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
print(sorted_data)



"""
Explanation of lambda in sorting:
A lambda function defines a small, anonymous function.
In the context of key for sorting, the lambda function takes a single argument (representing an element from the list/iterable) and returns a value that will be used for comparison during the sorting process.
This allows for flexible sorting based on specific attributes or calculated values of the elements, rather than just their default comparison.
The reverse=True argument can be added to both sorted() and .sort() to achieve descending order.
"""