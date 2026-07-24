"""
Title: Maximum Sum Subarray of Size K

Problem Statement:  
Given an array of positive integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Example 1:

Code
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5,1,3] has the maximum sum = 9.
Example 2:

Code
Input: nums = [2, 3, 4, 1, 5], k = 2
Output: 7
Explanation: Subarray [3,4] has the maximum sum = 7.

"""


def MaxSubarray(nums, k):
    left = 0
    cur_sum = 0
    max_sum = 0
    
    for right in range(len(nums)):
        cur_sum += nums[right]
        
        while right - left + 1 > k:
            cur_sum -= nums[left]
            left += 1
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(MaxSubarray([2, 1, 5, 1, 3, 2],3))
