# - Problem: Given an array of positive integers and a target sum, find the length of the largest contiguous subarray whose sum is lesser than the target. Return 0 if no such subarray exists.


def largest_subarray(nums, k):
    
    left =0
    current_sum = 0
    max_length = 0
    
    for right in range(len(nums)):
        
            
        current_sum += nums[right]
        while current_sum > k:
            
            current_sum -= nums[left]
            left += 1
            
        curr_length = right - left + 1
        max_length = max(max_length, curr_length)
    return max_length

        
print(largest_subarray([2, 1, 5, 2, 2, 2,  1, 3], 7)) 
        