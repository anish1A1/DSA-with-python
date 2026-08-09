"""
📝 Problem Statement
Given an array nums and a value val, remove all instances of val in‑place and return the new length.
The order of elements may be changed, but it doesn’t matter what you leave beyond the new length.

Example
Code
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
"""

def removeVal(nums, val):
    
    left = 0
    
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    
    return left

print(removeVal(nums = [3,2,2,3,2, 2, 3], val = 3))

# Use fast and slow two pointer