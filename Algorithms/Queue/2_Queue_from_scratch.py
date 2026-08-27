
# IMplementing queue from scratch.

class Queue:
    def __init__(self, size: int):
        self.queue = [None] * size  #Fixed-size array
        self.front = -1             #index of front element
        self.rear = -1              #index of the rear element
        self.size = size

    # Since at start, the queue is Empty, we used -1 a special marker meaning "empty queue".
    
    def isEmpty(self) -> bool:
        return self.front == -1
    
    def isFull(self) -> bool:
        return self.rear == self.size - 1
    
    def enqueue(self, value: int) ->None:
        if self.isFull():
            print("Queue is Full!")
            return 
        if self.isEmpty():
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = value 
    
    def dequeue(self) -> None:
        if self.isEmpty():
            print("Queue is Empty!")
            return
        print("Dequed", self.queue[self.front])
        self.front += 1
        
        if self.front > self.rear:  
            # Reset when queue becomes empty.
            self.front = self.rear = -1
        
    def peek(self) -> bool:
        if self.isEmpty():
            print("Queue is Empty!")
            return    
        return self.queue[self.front]
    
    def display(self) -> None:
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print("Queue elements: ", self.queue[self.front : self.rear + 1])

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()        # Queue elements: [10, 20, 30]
print(q.peek())    # 10
q.dequeue()        # Dequeued: 10
q.display()        # Queue elements: [20, 30]
