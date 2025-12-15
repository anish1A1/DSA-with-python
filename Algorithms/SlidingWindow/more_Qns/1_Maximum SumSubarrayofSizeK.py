"""
1. Maximum Sum Subarray of Size K

Difficulty: Easy

Problem

Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Example
Input: nums = [2,1,5,1,3,2], k = 3
Output: 9
Explanation: Subarray [5,1,3] has the maximum sum.
"""

def MaxSum(nums, k):
    left = 0
    max_sum = 0
    cur_sum = 0
    
    for right in range(len(nums)):
        cur_sum += nums[right]
        
        if right - left + 1 > k:
            cur_sum -= nums[left]
            left += 1
        
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(f"The max value is {MaxSum([2,1,5,1,3,2], 3)}")