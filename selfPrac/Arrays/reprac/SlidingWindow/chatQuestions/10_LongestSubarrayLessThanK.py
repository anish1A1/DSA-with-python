"""
Core Problem
Given an array of positive integers and an integer K, find the length of the longest contiguous subarray whose sum is ≤ K.

 Variant 1: Positive Integers Only
Approach: Sliding Window

Since all numbers are positive, the sum only increases when you expand the window.

If the sum exceeds K, shrink from the left until it’s ≤ K again.

Track the maximum window length.
"""

def longestSubarrayPos(nums, k):
    left = 0
    max_length = 0
    window_sum = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum > k:
            window_sum -= nums[left]
            left += 1
            
        max_length = max(max_length, right - left + 1)
    return max_length

print(longestSubarrayPos([2,1,5,2,2,2,1,3], 7))  # 4