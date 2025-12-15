"""
2. Maximum Average Subarray I (LeetCode 643)

Difficulty: Easy

Problem

Given an integer array nums and an integer k, find the maximum average value of a subarray of length k.

Example
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
"""


def Max_Average(nums, k):
    
    current_sum = sum(nums[:k])
    max_average = current_sum / float(k)
    
    for right in range(k, len(nums)):
        current_sum += nums[right]
        current_sum -= nums[right - k]
        sec_average = current_sum / float(k)
        
        max_average = max(max_average, sec_average)
        
    return max_average

print(f"The Max Average is {Max_Average([1,12,-5,-6,50,3], k = 4)}")