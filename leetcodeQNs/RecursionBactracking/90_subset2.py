"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order. 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[]
        nums.sort()

        def dfs(i, subset):

            if i == len(nums):
                result.append(subset[::])
                return
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()

            # We need to check the repeating value and if it occurs then we need to skip it
            while(i +1 < len(nums) and nums[i] == nums[i + 1]):
                i += 1
            dfs(i + 1, subset)
        dfs(0, [])
        return result

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 2]
    output = obj.subsetsWithDup(nums)
    print("Subsets (no duplicates):")
    for o in output:
        print(o)

