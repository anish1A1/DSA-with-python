# Traversal means traversing from head (first Node) to the next node until None.

# Define a Node
class Node:
    def __init__(self, data):
        self.data = data   # store the value
        self.next = None   # pointer to next node (Initially Empty)
        
# Define a Linked List
class LinkedList:
    def __init__(self):
        self.head = None   #Start with empty list
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:   #if list is empty
            self.head = new_node
            return
        
        temp = self.head   #1st
        while temp.next:   #2nd
            temp = temp.next   #3rd
        temp.next = new_node  # 4th
        # Linked new node at the end
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end= ' -> ')
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display() 
        
#1 = our first node; storing in temp
#2nd = loop from the 1st head untill the last Node whose next is not None.   
#3rd = store temp as temp.next node 
# 4th = since we store temp as temp.next we can add the new_node as its value (pointer to next node.)

"""
Step-by-Step
temp = self.head

temp points to the very first node (head).
Example list:

Code
10 -> 20 -> 30 -> None
→ temp points to 10.

while temp.next:
As long as there is a next node, keep moving forward.
This loop ensures you stop at the last node.
temp = temp.next

Move temp forward one step each time.

First iteration: temp becomes 20.
Second iteration: temp becomes 30.
Now temp.next is None, so the loop stops.

👉 At this point, temp points to the last node (30).
temp.next = new_node
Now we attach the new node at the end.

Important: temp is the last node (30).
temp.next was None.
We set it to new_node.

Result:
10 -> 20 -> 30 -> 40 -> None
"""
     
