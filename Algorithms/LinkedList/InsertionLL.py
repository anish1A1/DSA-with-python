

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)        
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at beginning")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as head (list was empty)")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at end")
    
    def insert_after_value(self, target, data):
        new_node = Node(data)
        # if the first node is target
        if self.head.data == target:
            # insert data between 1st node and sec. node.
            new_node.next = self.head.next
            self.head.next = new_node
            print(f"Inserted {data} after {target}")
            return
        
        temp = self.head
        while temp and temp.data !=target:
            temp = temp.next
            # linking temp with temp.next to go through all values.
            
        if temp is None:
            print(f"Value {target} not found")
            return
        # there is a target
        print(f"Inserted {data} after {target}")
        new_node.next = temp.next
        temp.next = new_node.next
       
       
    def insert_at_position(self, pos, data):
        new_node = Node(data)
        
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {pos}")
            return
        
        temp = self.head
        count = 0
        while temp and count < pos -1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range")
            return
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at position {pos}")
        
    def display(self):
        if self.head is None:
            print("Nothing to display, list is empty.")
            return
        temp = self.head
            
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")
        
ll = LinkedList()
ll.insert_at_beginning(10)   # 10 -> None
ll.insert_at_end(20)         # 10 -> 20 -> None
ll.insert_at_end(30)         # 10 -> 20 -> 30 -> None
ll.insert_after_value(20, 25) # 10 -> 20 -> 25 -> 30 -> None
ll.insert_at_position(2, 15)  # 10 -> 20 -> 15 -> 25 -> 30 -> None
ll.display()
