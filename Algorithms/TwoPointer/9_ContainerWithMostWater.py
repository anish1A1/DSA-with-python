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
Solution Approach (Two Pointers)
Intuition
The area between two lines is determined by:

Area
=
min
⁡
(
height[left]
,
height[right]
)
×
(
𝑟
𝑖
𝑔
ℎ
𝑡
−
𝑙
𝑒
𝑓
𝑡
)
To maximize area, we want:
A large width (right - left)
Tall heights (min(height[left], height[right]))

Strategy
Start with two pointers:

left = 0 (first line)
right = len(height) - 1 (last line)

Compute the area between them.
Move the pointer with the smaller height inward:

Because the limiting factor is the shorter line.
Moving the taller line inward won’t help (width decreases, height still limited).
Keep track of the maximum area seen.
Continue until left < right.


Area = width * minimum height of any one index. You will need bigger width to fill most water. Because the water can spill down you need the wall to be biggest.  The water can be most water only if the minimum height of any two pointer element times the width they cover in those pointer. 

We know that taking two pointer will be the best approach. We will start left from 0 and right from len(arr) - 1. We initialize an area = 0. Here we will store the area from the two pointers. The formula is width * height of  small wall of any element. after that we will use max_array object that will lookup for maximum value of area arr. To increase and decrease pointers we go with their wall height if left has small than change that pointer in this way we can solve this problem. The width of these pointer will be, right - left.

No, matter how big an element be inside two pointer, if its friend/pointer is small we will go with the small height because the water can only be filled uptill the smallest height practically.  Instead of L * B we should use width * min height of any one element.  The water can cover only till the height of the wall. and the width will be, right - left.
"""