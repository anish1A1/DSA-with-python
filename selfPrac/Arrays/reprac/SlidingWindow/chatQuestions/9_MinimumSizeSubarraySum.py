"""
Problem Statement
Given an array of positive integers nums and an integer target, return the minimal length of a contiguous subarray of which the sum is greater than or equal to target.
If there is no such subarray, return 0.

Example 1
Code
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has sum = 7 and length = 2.

Example 2
Code
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
Explanation: No subarray has sum ≥ 11.
✅ Sliding Window Solution (O(n))

"""

def minSubArrayLen(num, target):
    left = 0
    min_length = float('inf')
    window_sum = 0
    
    for right in range(len(num)):
        window_sum += num[right]
        
        while window_sum >= target :
            
            min_length = min(min_length, right - left + 1)
            window_sum -= num[left]
            left += 1
    
    
    return 0 if min_length == float('inf') else min_length

print(minSubArrayLen(target = 7, num = [2,3,1,2,4,3]))
print(minSubArrayLen(target = 11, num = [1,1,1,1,1,1,1,1])) # 0 
    