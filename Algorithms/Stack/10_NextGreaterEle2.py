"""
503. Next Greater Element II
Medium

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    
    stack = []
    answer = [-1] * len(nums)
    n = len(nums)
    
    for i in range(2*n):

        # Because we need circular array.
        # We only loop the circular array till the current element is found in merged array. So,
        
        num = nums[i % n]
        # This will give circular element from the merged array.
        # if len of array is 5, and now we go to 6th element, num ensures that
        # ongoing elements remain valid, it will make the 6th element index 0. and returns its element.
        
        while stack and num > nums[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = num
            
        if i < n:
            stack.append(i)
        # Only append the element till the length of the original array.
        
    return answer

print(nextGreaterElements([1,2,1]))       # [2, -1, 2]
print(nextGreaterElements([5,4,3,2,1]))   # [-1, 5, 5, 5, 5]
print(nextGreaterElements([2,1,2,4,3]))   # [4, 2, 4, -1, 4]


# Creating a circular array

print('Creating a circular array')

players = ["Alice", "Bob", "Charlie"]
total_players = len(players)

for i in range(2*total_players):
    current_player = players[i % total_players]
    
    print(f"Turn {i} : {current_player}")
