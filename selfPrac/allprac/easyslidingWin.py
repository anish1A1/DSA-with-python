# 
# Problem 1: Maximum Sum Subarray of Size K
# Problem Statement

# Given an array of integers nums and a positive integer k, find the maximum sum of any contiguous subarray of size exactly k.

# Examples

# Input	Output	Explanation
# nums = [2, 1, 5, 1, 3, 2], k = 3	9	The subarray [5, 1, 3] gives the maximum sum of 9.
# nums = [2, 3, 4, 1, 5], k = 2 	7	The subarray [3, 4] gives the maximum sum of 7.


# Constraints

# • 1 ≤ nums.length ≤ 10⁵
# • \(-10^4 \le \text{nums}[i] \le 10^4\)
# • 1 ≤ k ≤ nums.length

# Expected Complexities

# • Time Complexity: O(N)
# • Space Complexity: O(1)


def max_sum_subarray(arr, k):
    left = 0
    max_value = float('-inf')
    window_value = 0
    
    for right in range(len(arr)):
        window_value += arr[right]
        
        if right -left + 1 > k:
            window_value -= arr[left]
            left += 1
        
        max_value = max(max_value, window_value)
    return max_value

print(max_sum_subarray([2, 1, 5, 1, 3, 2], k = 3))    

