"""
3. Smallest Subarray with Sum ≥ Target

- Problem: Given an array of positive integers and a target sum, find the length of the smallest contiguous subarray whose sum is greater than or equal to the target. Return 0 if no such subarray exists.

- Example:
- Input: arr = [2, 1, 5, 2, 3, 2], target = 7
- Output: 2 (subarray [5,2])
"""

def Smallest_subarray(nums, k):
    left = 0
    min_length = float('inf')
    curr_sum = 0
    curr_length = 0
    
    for right in range(len(nums)):
        curr_sum += nums[right]
        
        while curr_sum >= k:
            
            curr_length = right - left + 1
            min_length = min(min_length, curr_length)
            curr_sum -= nums[left]
            left += 1
    
    return min_length

print(Smallest_subarray([2, 1, 5, 2, 3, 2],7))