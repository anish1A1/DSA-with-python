"""
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""

def checkFlagColor(nums):
    left = 0    #we will use left to check 0's color
    right = len(nums) - 1   #we will use right to check the 2's color    
    
    middle_pointer = 0     #this will be the pointer that checks the condition of element (fast pointer)
    # also it will act as pointer to check 1's 

# we know that middle_pointer (1's checker) will be less than right pointer(2's checker) since, 1,1,2,2. 

    while middle_pointer <= right:   
        if nums[middle_pointer] == 0:
            nums[left], nums[middle_pointer] = nums[middle_pointer], nums[left]   #since in-place sort
            left += 1
            middle_pointer += 1
        
        elif nums[middle_pointer] == 1:
            middle_pointer += 1
        else:
            nums[middle_pointer], nums[right] = nums[right], nums[middle_pointer]
            right -= 1
            # Here we will not increment middle_pointer because we are not counting the right elements/indexes
            
    return nums
print(checkFlagColor(nums = [2,0,2,1,1,0]))
print(checkFlagColor(nums = [2,0,1]))

            

"""
This problem can also be done with merge sort with 0(nlogn) time.
Also can be done in counting sort. (but needs two pass meaning two time array traversal.)

It can also be done in above method, 
We know that there is only three elememts to keep track of,
if we sort the 2 ( 0's) and 2 (2's) then automatically the 1's get sorted ,

To do this we need 3 pointers, left, right and middle_pointer.
Left for 0's Track.
right for 2's Track.  (We need to add 2 in last so, we take its last index).
Then middle_pointer, this is a fast pointer which will loop through array.

If the middle_pointer reaches 5 or greater then we know that index is of 2's (i.e left) so stop array there.
so, we used   while middle_pointer <= right:  , so loop will run till 1's last index only.

first we will check if current element is 0, if it is than swap the current element with left pointer.
if nums[middle_pointer] == 0:
    nums[left], nums[middle_pointer] = nums[middle_pointer], nums[left]

then increment left and middle_pointer pointer.

if current_element is 1, then do nothing just increment the middle_pointer by 1.
Because after left and right gets sorted 1's position will be automatically sorted.

then if, current element is 2, then swap the current element and right element.
and decrease its value.
We did not increase the middle_pointer value because we are not keeping track of 2's index by left pointer or middle_pointer.
So only decrease the right pointer by 1.



Now the whole array is sorted in place.
 

We will keep track of 0

"""