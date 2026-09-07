# Deletion means removing a node from the chain
# There are 3 common ways
# 1. Delete at the begining (remove head)
# 2. Delete at the end (remove last node)
# 3. Delete in the middle (remove a node by a value or position).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next 
        temp.next = new_node

    # Deleting at the begining
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        print(f'Deleted {self.head.data} from begining')
        self.head = self.head.next
        
    def delete_at_end(self):
        
        # check if list is empty
        if self.head is None:
            print("List is empty, nothing to delete")
            return  
        
        # if there is no second Node than
        if self.head.next is None:
            print(f"Deleted {self.head.data} from end")
            self.head.data = None
            return
        
        # there are more than 1 node, going to end. 
        temp = self.head
        while temp.next.next:  #went to last node.
            temp = temp.next   #stored temp with sec. last node.
        print(f"Deleted {temp.next.data} from end.")
        temp.next = None
        
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        
        # Check if first Node/head is value
        if self.head.data == value:
            print(f"Deleted {value} from list")
            self.head = self.head.next
        
        # Else, find the value
        temp = self.head
        # if temp.next.data gets value, loop will break. 
        # and temp stores node of 1 step previous value node.
        while temp.next and temp.next.data != value:
            temp = temp.next
        # we got value or the next is empty.
        if temp.next is None:
            print(f"Value {value} not found in List")
        else:
            print(f"Deleted {value} from List")
            temp.next = temp.next.next
    
    def display(self):
        if self.head is None:
            print("Nothing to display, list is empty.")
            return
        temp = self.head
        
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()          # 10 -> 20 -> 30 -> 40 -> None

ll.delete_at_beginning()  # Deleted 10
ll.display()              # 20 -> 30 -> 40 -> None

ll.delete_at_end()        # Deleted 40
ll.display()              # 20 -> 30 -> None

ll.delete_by_value(30)    # Deleted 30
ll.display()              # 20 -> None

"""
Value               Space    Time
Insert at beginning	O(1)   | O(1)
Insert at end (no tail)	O(n)| O(1)
Insert at end (with tail) O(1) |  O(1)
Delete at beginning	O(1)  |	O(1)
Delete at end	    O(n)  |	O(1)
Delete by value	    O(n)  |	O(1)
"""

# For Delete at end.
"""
1. while temp.next.next: temp = temp.next
This is used in delete at end.

temp starts at the head.
temp.next is the next node.

temp.next.next means “the node after the next one.”
So why do we check while temp.next.next?

Because we want to stop at the second-last node.
If you only did while temp.next, you'd end up at the last node.

But to delete the last node, you need to be at the node before it, so you can set its .next = None.

👉 Example:
List = 10 -> 20 -> 30 -> None
temp starts at 10.
temp.next.next exists (20 → 30), so move to 20.
At 20, temp.next.next is None (because 30 → None). Stop.

Now temp is at 20 (second last).
Do temp.next = None → removes 30.
"""

# For Delete by value
"""
The Code Again
python
temp = self.head
while temp.next and temp.next.data != value:
    temp = temp.next
🛠 What != Means
!= means “not equal to” in Python.

So temp.next.data != value means:
→ “The next node’s data is not equal to the value we want to delete.”

🔎 Why We Use It Here
We’re trying to find the node before the one we want to delete.

Suppose the list is:

Code
10 -> 20 -> 30 -> 40 -> None
and we want to delete 30.

Start at head (10).

Check: temp.next.data != 30 → 20 != 30 → True → move forward.

Now temp points to 20.

Check again: temp.next.data != 30 → 30 != 30 → False → stop.

Now temp points to 20, which is the node just before the one we want to delete.
That’s exactly where we need to be, so we can do:

temp.next = temp.next.next
This skips over 30 and links 20 directly to 40.
"""