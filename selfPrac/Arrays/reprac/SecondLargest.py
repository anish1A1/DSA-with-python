"""
Find Second Smallest and Second Largest Element in an array


Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Examples

Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
"""


def second_value(nums):
    
    if len(nums) < 2:
        return -1, -1
    
    smallest = float('inf')
    largest = float('-inf')
    s_smallest, s_largest = smallest, largest
    
    for i in nums:
        if largest < i:
            s_largest = largest
            largest = i
        
        elif largest > i and i > s_largest:
            s_largest = i 
        
        if smallest > i:
            s_smallest = smallest
            smallest = i
        
        elif smallest < i and s_smallest > i:
            s_smallest = i 
        
    return largest, smallest, s_smallest, s_largest

input =[1,2,4,7,7,5,6,6]
print(second_value(input))
 