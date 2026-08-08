"""
Problem Statement
Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non‑zero elements.
You must do this in‑place with O(1) extra space.

Example
Code
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

def moveZero(nums):
    left = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            
            nums[left] = nums[right]
            left += 1
    for i in range(left, len(nums)):
        nums[i] = 0
         
    return nums

print(moveZero([0,1,0,3,12]))

# used fast and slow two pointer