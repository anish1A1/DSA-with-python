"""
739. Daily Temperatures
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


# find the next greatest temperature of current i
# if found then after how many steps you took to find it return it.

def dailyTemperature(temperature):
    
    stack = []
    answer = [0] * len(temperature)
    
    for i in range(len(temperature)):
        
        while stack and temperature[i] > temperature[stack[-1]]:
            
            prev_index = stack.pop()
            # since we need answer to have total step taken for each element to get the greater element so,
            
            answer[prev_index] = i - prev_index
            
            # i is the current index, prev_index is the previous greatest element index.
            # so answer[prev_index] is the step of these both
            
        stack.append(i)
    return answer


# Example tests
print(dailyTemperature([73,74,75,71,69,72,76,73]))  
# Output: [1,1,4,2,1,1,0,0]
print(dailyTemperature([30,40,50,60]))  
# Output: [1,1,1,0]
print(dailyTemperature([30,60,90]))  
# Output: [1,1,0]