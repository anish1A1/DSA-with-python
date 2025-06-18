from collections import deque

arr = [[0] *4 for i in range(4)]
print(arr[1])

arr[1]= [1,1,1,1] 
print(arr)

strings = ["ab", "cd", "ef"]
print("". join(strings))



queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(4)

print(queue)

queue.pop()
print(queue)


# HashSet   {}  
# We use hashset as it will not contain any duplicate values
# to use Hashset aka set we allways define set()

mySet = set()

mySet.add(1)
mySet.add(2)

print(f"\n {mySet}")
print(2 in mySet)  

mySet.remove(2)
print(mySet)



print(set([5,6,7]))

loopset = {i for i in range(5)}
print(loopset)

print("\n")

# Hashmap (aka dictionary)
# We can define a dict using empty curly braces too.
myMap = {}

myMap['aka'] = 23
myMap['tom'] = 89

print(myMap)

print(myMap['aka'])
print("tom" in myMap)

myMap.pop("tom")
print(myMap)


# Dict comprehension

# allMap = {i:2  for i in range(4)}
allMap = {i:2*i  for i in range(4)}

print(allMap)
print("\n")
# Looping through dict.

for key in allMap:
    print(key, allMap[key])

for val in allMap.values():
    print(val)
for key,val in allMap.items():
    print(key, val)

print("\n")

# tuples

abc =(1,2,3)
# abc[0] = 1 # we cannot change tuples (immutable)
print(abc)

# We can use tuple to be used as key for hash map/set
newMap = {(1,2) : 'value'}
print(newMap)

newSet = set()
newSet.add((1,2))
print(newSet)

numbers = [1,2,3,4,5]
mergeSet = set(numbers)
print(mergeSet)