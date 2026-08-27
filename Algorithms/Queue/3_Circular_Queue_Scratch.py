"""
Queue Problem: Implement a Circular Queue

Problem
Design a data structure that works like a circular queue.
You need to support these operations:

enQueue(x) → insert an element into the queue.

deQueue() → delete an element from the queue.

Front() → get the front item.

Rear() → get the last item.

isEmpty() → check if the queue is empty.

isFull() → check if the queue is full.
"""

class MyCircularQueue:
    def __init__(self, k:int):
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
        print(f"Queue created with size {k}")

    def isEmpty(self) -> bool:
        empty = self.count == 0
        print("Queue is empty" if empty else "Queue is not empty")
        return empty

    def isFull(self) -> bool:
        full = self.count == self.size
        print("Queue is full" if full else "Queue is not full")
        return full

    def enQueue(self, value:int) -> bool:
        if self.isFull():
            print(f"Cannot enqueue {value}: Queue is full")
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        print(f"Enqueued {value} at position {self.rear}")
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            print("Cannot dequeue: Queue is empty")
            return False
        removed = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        print(f"Dequeued {removed} from position {(self.front - 1) % self.size}")
        return True

    def Front(self):
        if self.isEmpty():
            print("Front element not available: Queue is empty")
            return -1
        print(f"Front element is {self.queue[self.front]}")
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            print("Rear element not available: Queue is empty")
            return -1
        print(f"Rear element is {self.queue[self.rear]}")
        return self.queue[self.rear]

q = MyCircularQueue(3)
q.enQueue(10)   # Enqueued 10 at position 0
q.enQueue(20)   # Enqueued 20 at position 1
q.enQueue(30)   # Enqueued 30 at position 2
q.enQueue(40)   # Cannot enqueue 40: Queue is full
q.Front()       # Front element is 10
q.Rear()        # Rear element is 30
q.deQueue()     # Dequeued 10 from position 0
q.enQueue(40)   # Enqueued 40 at position 0 (wrapped around)
q.Rear()        # Rear element is 40



# Also done


class MyCircularQueue:
    def __init__(self, k:int):
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def isEmpty(self) -> bool:
        return self.count == 0
    
    def isFull(self) -> bool:
        return self.count == self.size
    
    def enQueue(self, value:int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True
    
    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.front]
    
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]
    
q = MyCircularQueue(3)
print(q.enQueue(1))  # True
print(q.enQueue(2))  # True
print(q.enQueue(3))  # True
print(q.enQueue(4))  # False (queue full)
print(q.Rear())      # 3
print(q.isFull())    # True
print(q.deQueue())   # True
print(q.enQueue(4))  # True
print(q.Rear())      # 4
