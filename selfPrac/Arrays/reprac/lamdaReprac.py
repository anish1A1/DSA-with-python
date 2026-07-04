list1 = [2,4,5,6,722,33,53]

list1.sort(key=lambda x: x > 50)
print(list1) 

data = [('apple', 3), ('banana', 1), ('cherry', 2)]

sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
# Sort based on 2nd index value

numbers = [{'value': 10}, {'value': 5}, {'value': 15}]

numbers.sort(key=lambda x: x['value'])
print(numbers)


people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

people.sort(key= lambda x : x['age'])
print(people)


data = [('apple', 5), ('kiwi', 7),('banana', 2), ('cherry', 8)]
data.sort(key= lambda x: x[0], reverse=True)
print(data)

square = lambda x: x**2
print(square(4))