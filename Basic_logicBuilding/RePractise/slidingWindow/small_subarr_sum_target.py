"""
3. Smallest Subarray with Sum ≥ Target

- Problem: Given an array of positive integers and a target sum, find the length of the smallest contiguous subarray whose sum is greater than or equal to the target. Return 0 if no such subarray exists.

- Example:
- Input: arr = [2, 1, 5, 2, 3, 2], target = 7
- Output: 2 (subarray [5,2])
"""

def small_subarr_sum_gtr_eql_to_target(arr, target):
    window_sum = 0
    min_length = float("inf")
    cur_length = 0
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= target:
            cur_length = right - left + 1
            min_length = min(min_length, cur_length)
            window_sum -= arr[left]
            left +=1
            
    return 0 if min_length == float("inf") else min_length
print(small_subarr_sum_gtr_eql_to_target(arr = [2, 1, 5, 2, 3, 2], target = 7))


def bruteforce_subarr(arr, target):
    n = len(arr)
    min_length = float("inf")
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            
            if current_sum >= target:
                current_sum = j - i + 1
                min_length = min(min_length, current_sum)
                break
    return 0 if min_length == float("inf") else min_length
print(bruteforce_subarr(arr = [2, 1, 5, 2, 3, 2], target = 7))    