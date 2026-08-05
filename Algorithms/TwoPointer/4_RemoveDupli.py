"""
📝 Problem Statement
Given a sorted array nums, remove the duplicates in‑place such that each unique element appears only once.
Return the new length of the array.
The relative order of the elements should be kept the same.
You must do this with O(1) extra space.

Example
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

"""


# Using Two pointer approach same direction.
def rem_duplicates(nums):
    
    if not nums:
        return 0
    
    # left will track the placement for unique elmnt
    left = 1
    
    for right in range(1, len(nums)):
        
        # If there is unique element than put that element in left index.
        
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    # return left  #or
    return nums[:left]
    
print(rem_duplicates([0,0,0,1,1,1,2,2,3,3,4]))
 
# Time => 0(n), space => 0(1)



# Solution class containing removeDuplicates method
class Solution:
    # Removes duplicates using set and returns count of unique elements
    def removeDuplicates(self, nums):
        # Set to store seen unique elements
        seen = set()

        # Position to overwrite next unique element
        left = 0

        # Iterate over each number in nums
        for right in nums:
            # If right is not in seen, it is unique
            if right not in seen:
                # Add num to set
                seen.add(right)

                # Overwrite nums[index] with this current value.
                nums[left] = right

                # Move index forward
                left += 1
            

        # Return number of unique elements
        return left


# Driver code
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)

print("k =", k)
print("Array after removing duplicates:", nums[:k])


# Space => 0(n), Time => 0(n)

 