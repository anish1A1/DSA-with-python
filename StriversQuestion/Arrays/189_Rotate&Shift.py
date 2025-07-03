
"""

189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 
"""


def rotate_ShiftArray(nums, k):
    
    n = len(nums)
    if n < 2:
        return -1
    
    
    k = k % n
    
    def swapper(start, end):
        
        while start < end:
            
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -=1
            
            
    swapper(0, n - 1)
    swapper(0, k-1)
    swapper(k, n-1)
    return nums

    

arr = [1,2,3,4,5,6]
k = 3

print(rotate_ShiftArray(arr, k)) 


"""

        Here we will first take the remainder by k = k % n    for e.g 3 % 7 => 3,

        then make a swapper function which will swap start and end values
        after swapping the start and end indexes will increment and decrement respectively

        We will call swapper function three time 
        One to reverse all the array --> [1,2,3,4,5]  => [5,4,3,2,1]
        Then another to sort the array till k_th element--> [5,4,3,2,1] if k=2 then [5,4,1,2,3]
        Then another to sort the remaining array => [5,4,1,2,3]
"""