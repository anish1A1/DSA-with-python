"""
1. Maximum Sum Subarray of Size K
- Problem: Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

- Example:
- Input: arr = [2, 1, 5, 1, 3, 2], k = 3
- Output: 9 (subarray [5,1,3])

"""

def max_sum_array(arr, k):
    curr_sum = 0
    left = 0
    max_sum = 0
    
    for right in range(len(arr)):
        curr_sum += arr[right]
        
        if right - left + 1 == k:
            max_sum = max(curr_sum, max_sum)
            curr_sum -= arr[left]
            left+=1
    return max_sum
print(max_sum_array( [2, 1, 5, 1, 3, 2], k = 3))
            