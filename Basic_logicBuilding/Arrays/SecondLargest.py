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
def secLar(arr):
    
    
    n = len(arr)
    if n < 2 :
        return -1
    
    largest = float('-inf')
    s_largest = float('-inf')
    
    for i in range(n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
            
        elif largest > arr[i] and arr[i] > s_largest:
            s_largest = arr[i]     
            
        
    return s_largest

Input = [1,1,2,4,7,7,5]
print(f"{secLar(Input)}")