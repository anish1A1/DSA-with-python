
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sums = nums[left] + nums[right]
        
        if sums == target:
            return [left + 1, right + 1]
        elif sums < target:
            left += 1
        else:
            right -= 1
    return 0, 0
print(twoSum([2,7,11,15], target = 9))