
"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums

        ins_posn = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[ins_posn] = nums[i]
                ins_posn +=1
        
        for i in range(ins_posn, n):
            nums[i] = 0
        return nums


mth = Solution()
arrs= [1,0,3,0,6,7,0]
print(mth.moveZeroes(arrs))
        