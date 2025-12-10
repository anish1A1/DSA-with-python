"""
Largest Element
Easy
Given an array of integers nums, return the value of the largest element in the array

Examples:

Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6

Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99
"""


def LarElement(arr):
    largest = arr[0]
    # if len(arr) < 1:
    #     return largest
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
    return largest

print(LarElement([3, 3, 0, 99, -40]))


