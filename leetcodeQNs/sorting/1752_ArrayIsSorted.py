
"""
1752. Check if Array Is Sorted and Rotated

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 

"""


def checkArray(arr):
    
    n =len(arr)
    count = 1 
    
    if n < 2:
        return True
    for i in range(1, n):
        if arr[(i -1) % 2] < arr[i % 2]:
            count += 1
        
        else:
            count = 1
    
        if count == n:
            return True
    return False

nums = [3,4,5,1,2]
nums2 = [2,1,3,4]

print(f"For rotated array : {checkArray(nums)}")
print(f"For unrotated array : {checkArray(nums2)}")





"""
We can solve this problem in many ways but the most efficient way would be by thinking like this,
nums = [3,4,5,1,2, 2]

Here what if we add the [3,4,5,1,2, 2] with again [3,4,5,1,2, 2]
So it would be [3,4,5,1,2, 2, 3,4,5,1,2, 2] 

Here look carefully,  [3,4,5,1,2, 2, 3,4,5,1,2, 2]. Here the array can be found sorted here. This rotated array can be solved by thinking in this way. 

We will start a count = 1 (index 0), (at first)
If there is any number which will be less than than the current index than the count will restart and will be set to 1 again.
now when the count reaches the length of original array i.e. 6 for this,  for e.g  count == 6 then the array has the sorted/rotated array. Since The array length is 6 and the count has also become 6 this means there is the whole sorted array available in this array. So we return True.

To make this happen we will loop a array 2 time the array and start from index 1. Then we will check the first index [i-1] is less than or equal to the i index. 
Here remember that we are looping from 2 * n (2 times size of array) so, we can occur the index out of bound error. 
To fix this we can use modulas (this will help with the index of the array) 
for e.g. [3,4,5,1,2, 2, 3,4,5,1,2, 2].  Here when going to 3 (of index 7) Index out of bound error will arise so, we will use the modulas to fix our indexing.
If gone to three it will become index 1 by using modulas.
arr[(i – 1) % n]   so for this it will become   7/5  when using modulas it will be 1. Since to divide 7 by 5. 5 can only be used once.
 

"""