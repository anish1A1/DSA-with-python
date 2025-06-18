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


# Hashmap (aka dictionary)