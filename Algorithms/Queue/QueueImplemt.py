# Queue --> FIFO (First In First Out)

from collections import deque

queue = deque()

# Enqueue
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
print(queue)


# From/Peek
print(queue[0])


# Deque
queue.popleft()
queue.popleft()
print(queue)

# Is Empty
print(len(queue))
