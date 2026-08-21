"""
155. Min Stack
Medium

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or self.minStack[-1] >= value:
            self.minStack.append(value)

    def pop(self) -> None:
        cur_el = self.stack.pop()
        if cur_el == self.minStack[-1]:
            self.minStack.pop()
            # Only remove value of minStack if the current element of stack is equal to the
            # last element of minStack.
            
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())  # -3
obj.pop()            # removes -3
print(obj.top())     # 0
print(obj.getMin())  # -2
  