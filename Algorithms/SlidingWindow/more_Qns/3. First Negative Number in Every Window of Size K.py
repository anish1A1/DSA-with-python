"""
First Negative Number in Every Window of Size K

Difficulty: Medium

Problem

Given an array and a window size k, return the first negative number in every window of size k.
If no negative exists, return 0.

Example
Input: nums = [-8, 2, 3, -6, 10], k = 2
Output: [-8, 0, -6, -6]
"""

def FindNegInWindow(nums, k):
    left = 0
    neg_array = [] # we are storing the index of negative number
    result = []
    
    for right in range(len(nums)):
        if nums[right] < 0:
            neg_array.append(right)

        if right - left + 1 == k:
            if neg_array:
                result.append(nums[neg_array[0]])
            else:
                result.append(0)
            
            # If there is any negative number, and the index of negative number is equal to the 
            # left pointer we remove that, as done in sliding window.
            if neg_array and neg_array[0] == left:
                neg_array.pop(0) 
        
            left += 1
    return result
    
print(FindNegInWindow([-8, 2, 3, -6, 10], k = 3))