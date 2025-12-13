"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 
"""

def findmaxAverage(nums, k):
    current_sum = sum(nums[:k])
    # Will get all the value till the kth element and sums it up
    max_sum = current_sum

    # Creating a loop for the leftover elements
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        # Here we are adding the new element that is comming and also substracting the previous element. 
        max_sum = max(max_sum, current_sum)
        average = max_sum / k
    return average


print(findmaxAverage([1,2,3,4,5,6], 3))
    
         