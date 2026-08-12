"""
11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List

def maxArea(height:List[int]):
    left = 0
    right = len(height) - 1
    area = 0
    max_area = 0
    
    while left < right:
        area = (right - left) * min(height[left], height[right])
        # here width is right - left, the total distance between them
        max_area = max(area, max_area)
        
        if height[left] < height[right]:
            left += 1
        elif height[right] < height[left]:
            right -=1
        else:  #if element are equal move any one pointer.
            left += 1
            
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))


def maxAreaBrute(height: List[int]):  
    
    area = 0
    max_area = 0
    
    for i in range(len(height)):
        for j in range(i+1 ,len(height)):
            area = (j - i) * min(height[i], height[j])
            # j is the fast pointer. 
            # To get the width(total distance of each elements in i and j)-> j-i.
            
            max_area = max(max_area, area)
            
    return max_area

print(maxAreaBrute([1,8,6,2,5,4,8,3,7]))

"""

"""