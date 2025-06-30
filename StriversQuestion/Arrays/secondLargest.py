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

"""
For this question we will store the minimum value of largest and second largest in a variable and loop the array.

we will check if the arr's i is greater than largest if yes than add that to largest value.
Then we check if the largest is greater than i index value and agian the i is greater than the s_largest value.
"""


# Now finding the second smallest array.

def secondSmallest(arr):
    
    smallest = float('inf')
    s_smallest = float('inf')
    n =len(arr)
    if n < 2:
        return -1
    
    for i in range(n):
        
        if arr[i] < smallest:
            s_smallest = smallest
            smallest = arr[i]
        
        elif arr[i] < s_smallest and arr[i] > smallest:
            s_smallest = arr[i]
            
    return s_smallest

Input = [1,1,2,4,7,7,5]
print(f"{secondSmallest(Input)}")


"""
For this question we will store the maximum value of smallest and second smallest in a variable and loop the array.

we will check if the arr's i is less than smallest if yes than add that to smallest value.
Then we check if the i value is less than the second smallest aswell as check if that i is greater than smallest if yes than add that to s_smallest.
"""