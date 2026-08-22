"""
Given an array, for each element find the next greater element to its right.

If none exists, return -1 for that position.

Example:  
Input: [2, 1, 2, 4, 3]  
Output: [4, 2, 4, -1, -1]
"""


def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n   # default answer is -1
    stack = []          # stack will store indices

    for i in range(n):
        # While stack is not empty and current element is greater
        
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]   
            # update answer for that index
            
        stack.append(i)  # push current index

    return result

print(nextGreaterElements([2,1,2,4,3]))
# Output: [4, 2, 4, -1, -1]

    
"""
Step-by-Step Trace
Array: [2, 1, 2, 4, 3]

i=0 → push index 0 (value 2).
stack = [0]

i=1 → value 1 ≤ nums[0]=2 → push index 1.
stack = [0,1]

i=2 → value 2 > nums[1]=1 → pop index 1 → result[1]=2.
stack = [0] → push index 2.

i=3 → value 4 > nums[2]=2 → pop index 2 → result[2]=4.
value 4 > nums[0]=2 → pop index 0 → result[0]=4.
stack = [] → push index 3.

i=4 → value 3 ≤ nums[3]=4 → push index 4.
stack = [3,4]

End: indices 3 and 4 remain → result[3]=-1, result[4]=-1.

Final result = [4,2,4,-1,-1].

🎯 Key Catch
Stack stores indices so we can update the correct position in the result.

Each element is pushed once and popped once → O(n) time.

This is why indices are essential in stack problems like Next Greater Element.
"""