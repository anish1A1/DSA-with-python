"""
Check if the Array is Sorted II

Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
Examples:
Input : nums = [1, 2, 3, 4, 5]
Output : true
Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Input : nums = [1, 2, 1, 4, 5]
Output : false
Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

Input : nums = [1,9,6,8,5,4,0]
"""


def check_array_Is_Sorted(arrays) -> bool:
    len_array = len(arrays) - 1
    for i in range(len_array):
        if arrays[i] > arrays[i+1]:
            return False
        
    
    return True
print(check_array_Is_Sorted([1,9,6,8,5,4,0]))



# sort_ar = [1,9,6,8,5,4,0]
# print(sorted(sort_ar))