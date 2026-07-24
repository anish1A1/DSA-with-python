"""
Title: Average of Subarrays of Size K

Problem Statement:  
Given an array of positive integers nums and an integer k, find the average of all contiguous subarrays of size k. Return the result as a list of floating‑point numbers rounded to 2 decimal places.

Example 1:

Code
Input: nums = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
Explanation:
Subarrays of size 5 are:
[1,3,2,6,-1] → average = 2.2
[3,2,6,-1,4] → average = 2.8
[2,6,-1,4,1] → average = 2.4
[6,-1,4,1,8] → average = 3.6
[-1,4,1,8,2] → average = 2.8
Example 2:

Code
Input: nums = [5, 10, 15], k = 2
Output: [7.5, 12.5]
Constraints:

1 ≤ nums.length ≤ 10⁵

-10⁴ ≤ nums[i] ≤ 10⁴

1 ≤ k ≤ nums.length
"""

def avg_subarray_k(nums, k):
    
    avg_values = []
    window_sum = 0
    
    # for first window average
    for i in range(k):   #uptill k elements
        window_sum += nums[i]
    
    avg_values.append(round(window_sum / k, 2)) 
    #The second parameter of round helps to get the decimal value
    
    # now to get avg of all remaining window average
    
    for i in range(k, len(nums)):
        # print(i)
        window_sum += nums[i] - nums[i-k]  
        # here the index value of i is equal to the k because it did not start from first index of nums.
        #we need to substract previous value so added [i-k] for e.g. nums[5-5] 
        avg_values.append(round(window_sum / k, 2)) 
    
    return avg_values


print(avg_subarray_k([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))  
print(avg_subarray_k([5, 10, 15], 2))       


# Short way to do it

def avg_subarray_k_short(nums, k):
    
    avg_list = []
    
    window_sum = sum(nums[:k])
    
    avg_list.append(round((window_sum / k), 2))
    
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        avg_list.append(round((window_sum / k), 2))
    
    return avg_list

print('\n')
print(avg_subarray_k_short([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))  
print(avg_subarray_k_short([5, 10, 15], 2))  