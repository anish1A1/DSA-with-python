
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Doing with functions only.

def display(head):
    temp = head
    while temp:
        print(temp.data, end=' -> ')
        temp = temp.next
    print('None')


def reverse(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next   # save next
        current.next = prev        # reverse link
        prev = current             # move prev forward
        current = next_node        # move current forward
    
    return prev   # new head of reversed list


# Create nodes manually
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before reversal:")
display(head)

# Reverse
head = reverse(head)

print("After reversal:")
display(head)

print('\n')
print('With Class LL')
# Inside a class

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_value(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head 
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Added {data} in Linked List")
    
    # Reverse function
    def reverse(self):
        if self.head is None:
            print('Insert First to Reverse')
            return
        current = self.head
        prev = None
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        self.head = prev

    def display(self):
        if self.head is None:
            print('Add first to display')
            return

        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')


class_head = LinkedList()
class_head.add_value(10)
class_head.add_value(20)
class_head.add_value(30)

print("Before reversal:")
class_head.display()

print("After reversal:")
class_head.reverse()
display(head)


# completed 