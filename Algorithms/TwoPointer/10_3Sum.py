"""
15. 3Sum
Medium
Topics

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def sum3_optimal(nums):
    result = []
    nums.sort()
    
    for index, element in enumerate(nums):
        # check if second ongoing index is equal to previous ones. if yes skip it. 
        if index > 0 and nums[index - 1] == element:
            continue
        
        left = index + 1
        right = len(nums) - 1
        
        while left < right:
            total_sum = nums[left] + nums[right] + element
            
            if total_sum > 0:
                right -= 1
            elif total_sum < 0:
                left += 1
            else:
                result.append([element, nums[left], nums[right]]) 
                left += 1    #we always increase a pointer in each loop
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result
print("Optimal Solution")
print(sum3_optimal(nums = [-1,0,1,2,-1,-4]))
print(sum3_optimal(nums = [0,1,1]))
print(sum3_optimal(nums = [0,0,0]))

"""
while left < right and nums[left] == nums[left - 1]:
    left += 1
This loop skips duplicates:

After finding a valid triplet, if the next nums[left] is the same as the previous one, you’d get the same triplet again.
So you keep moving left forward until you hit a new value.
This ensures that each triplet in result is unique.
"""

def sum3_average(nums):

    result = set()
    nums.sort()
    for i in range(len(nums)):
        left = i + 1
        right= len(nums) - 1
        
        while left < right:
            if nums[i]+nums[left] + nums[right] == 0:
                triplets = tuple(sorted([nums[i], nums[left], nums[right]]))
                result.add(triplets)
            if nums[i]+nums[left] + nums[right] > 0:
                right -= 1
            else:
                left +=1  
    return [list(triplets) for triplets in result]
# We will take two pointers inside a loop
# Space 0(n²) Time O(n²) space (due to storing results)

print("Average Solution")
print(sum3_average(nums = [-1,0,1,2,-1,-4]))
print(sum3_average(nums = [0,1,1]))
print(sum3_average(nums = [0,0,0]))



def Sum3_Brute(nums):
    
    result =set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplets)
                    
                    """
                        This will sort the value (create a new array) and return the sorted element.
                        We will convert it in tuple to store in set. # '(-1,0,1)' and this will be added in set.
                        Lists are not hashable, so you can’t put them directly into a set.
                        Converting to a tuple makes it immutable and hashable, so it can be stored in a set.
                    """
                        
                    
    return [list(triplets) for triplets in result]
# Time 0(n3), Space 0(n3)
# This a list comprehension that converts each triplet (which is stored as a tuple inside the set) back into a list.
print("Brute force Solution")
print(Sum3_Brute(nums = [-1,0,1,2,-1,-4]))
print( Sum3_Brute(nums = [0,1,1]))
print(Sum3_Brute(nums = [0,0,0]))
    
"""
Step‑by‑Step Explanation
[nums[i], nums[j], nums[k]]

This is the raw triplet you found that sums to zero.
sorted([...])

Sorting ensures that the triplet always has the same order.
Example: [0,1,-1] becomes [-1,0,1].
Without sorting, [0,1,-1] and [-1,0,1] would be treated as different triplets even though they’re the same set of numbers.

tuple(...)
Lists are not hashable, so you can’t put them directly into a set.
Converting to a tuple makes it immutable and hashable, so it can be stored in a set.
result.add(triplet)

A set automatically removes duplicates.
If the same triplet appears again, it won’t be added twice.

Why This Fixes Your Brute Force
Your original brute force collected duplicates like [0,1,-1] and [-1,0,1].
By sorting and storing as a tuple in a set, you guarantee uniqueness.

At the end, you can convert the set back to a list of lists for the final answer.

Why This Fixes Your Brute Force:
Your original brute force collected duplicates like [0,1,-1] and [-1,0,1].
By sorting and storing as a tuple in a set, you guarantee uniqueness.
At the end, you can convert the set back to a list of lists for the final answer.
"""
    # This way didn't worked because it didn't showed unique values result. 
    # result =[]
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
                
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 result.append([nums[i], nums[j], nums[k]])
    # return result

