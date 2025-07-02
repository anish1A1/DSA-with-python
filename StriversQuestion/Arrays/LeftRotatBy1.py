"""
Left Rotate the Array by One


Problem Statement: Given an array of N integers, left rotate the array by one place.

Examples

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
Explanation: 
Since all the elements in array will be shifted 
toward left by one so ‘2’ will now become the 
first index and and ‘1’ which was present at 
first index will be shifted at last.


Example 2:
Input: N = 1, array[] = {3}
Output: 3
Explanation: Here only element is present and so 
the element at first index will be shifted to 
last index which is also by the way the first index.

"""

# using Brute force approach

def lefRot(arr, n):

    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
        
    # Now we add the first index of arr in temp to the last.
    temp[n - 1] = arr[0]
    
    return temp
# Time 0(n)  and  space 0(n)
 
num = [1,2,3,4,5]
print(lefRot(num, len(num)))


"""
Here this is not in place algo.. We just need to shift left element to right by only one time.  Here creating a empty array same as arr. Then we add the values of arr in temp starting from index 0 of temp (but we lopped from 1 index of arr.)
Then after the loop temp will look like [2,3,4,5]
Now we just need to start the first index of arr in temp. 
Then it will look [2,3,4,5,1]  
"""


# Using Optimal Approach

def opt_leftRot(arr, n):
    temp = arr[0]
    
    for i in range(n -1):
        arr[i] = arr[i + 1]
    
    arr[n - 1] = temp
    
    return arr
# Time Compl 0(n)   and  space 0(1)
num = [1,2,3,4,5]
print(opt_leftRot(num, len(num)))


"""
In this arroach we store the first index in a temp. variable then loop the array. We chnage the value of array to its index +1 value.

After loop we add the temp variable in the end of the array.

"""
