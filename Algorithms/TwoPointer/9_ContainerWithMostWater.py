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


def maxAreaBrute(height: List[int]):  
    
    area = 0
    max_area = 0
    
    for i in range(len(height)):
        for j in range(i+1 ,len(height)):
            area = (j - 1) * min(height[i], height[j])
            # since j is the fast pointer it's position will be the width. 
            # And also we added j by 1 to start brute force when reomved 1 we get its current array index.
            
            max_area = max(max_area, area)
            
    return max_area

print(maxAreaBrute([1,8,6,2,5,4,8,3,7]))

"""

"""