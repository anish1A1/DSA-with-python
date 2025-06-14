"""
To check an array is sorted
for e.g: a= [1,2,8,5,6]
Now to check if this is sorted or not if its value is increasing or same with ongoing index of array.

for above e.g the array is not sorted. 
Now make a algor. to check this.

This algo. should provide a bool value  
"""


def checkArraySrted (arr, n):
    if (n== 0 or n ==1):
       return True
   
    # arr[n-1] >= arr[n-2]
    # return checkArraySrted(arr, n-1)
# or
    return (arr[n-1] >= arr[n-2] and checkArraySrted(arr, n-1))

    # This will check from n-1 >= n-2 for e.g 5-1 >= 5-2 if true than return true. and the recursion is also added after that. if the codition returns false then, the recursion will not have to run. 
    # We are using and operator if one cond. is false all condition is false. so, if arr[n-1] >= arr[n-2] return false than we do not need to check again and again by making recursive calls.
    
    # The array is not sorted if cond. return false
    
    
n = [1,2,8,4,5]
print("\n")
# Time and space complexity fro this recursion is O(n)
print(f"Using recursive way: It returns  {checkArraySrted(n, len(n))}")

print("\n")



"""
Using Iterative way to solve this sorting problem

"""
def isSortedIterative(arr):
    for i in range( len(arr)-1):    # correctly loop within bound as    arr[i+1] is checking the last index of array too. so, we are using len(arr-1) here.
        # range works from 0 to n-1 for this
        
        if arr[i] > arr[i+1]:  # check if i >= i+1 index value of array 
            
            return False   # if i is greater return False
    
    return True    # if i is not greater than i +1 than array is sorted.

print(f"Using iterative way: It returns  {isSortedIterative([1,2,8,4,5])}")