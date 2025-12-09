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



def Sec_small_lar(arr):
    smallest= s_smallest = float('inf')
    largest = s_largest = float('-inf')
    
    if len(arr) < 2:
        return -1
    
    for i in arr:
        if i < smallest:
            s_smallest = smallest
            smallest = i
        elif smallest < i <s_smallest:
            s_smallest =i
        
        
        if i > largest:
            s_largest = largest
            largest = i
        elif largest > i > s_largest:
            s_largest =i 
    
    if s_largest == s_smallest:
        return -1,-1
    
    return s_smallest, s_largest

print(Sec_small_lar([1,2,4,7,7,5,6]))

"""
O(n) time

O(1) extra space

Does NOT require sorting

Handles duplicates correctly

Matches real interview expectations
"""