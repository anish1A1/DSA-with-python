"""
Problem Statement
You’re given a sorted array of integers numbers (1-indexed) and a target integer target.
Return the indices of the two numbers such that they add up to target.
You must use exactly one element twice, and the solution is guaranteed to exist.

Example
Code
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: numbers[1] + numbers[2] = 2 + 7 = 9
"""

def twoSumIndex(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        
        current_sum = nums [left] + nums[right]

        if current_sum == target:
            return [left+ 1, right + 1] # 1-indexed
        
        elif current_sum < target:
            left += 1 
        else:
            right -= 1
    return 0
print(twoSumIndex(nums = [2,7,11,15], target = 9))