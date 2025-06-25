
"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
"""

class Solution(object):
    def merge(self, intervals):
        
        intervals.sort(key=lambda first_elemnt: first_elemnt[0])
        
        overlapping_array = []
    
        for interval in intervals:
            if not overlapping_array or overlapping_array[-1][1] < interval[0]:
                
                overlapping_array.append(interval)
                # here first element is added first after that checks if overlapping araay second element is greater than interval first element. if not add that interval
            
            else:
                overlapping_array[-1][1] = max(overlapping_array[-1][1], interval[1])
                
        return overlapping_array


answer = Solution()
list= [[1,3],[2,6],[8,10],[15,18]]
output = answer.merge(list)

print(output)
                
                
                
"""
class Solution(object):

    # We know that to fall in overlapping interval the first element 2nd index first[0][1] should not be greater than second element first index second[0]  for eg. [1,3] and [2,6] here 3 is not greater than the 2.


    def merge(self, intervals):
        
        # at first we have to sort for e.g if unsorted list is given then our code will not work
        
        intervals.sort(key=lambda first_element: first_element[0])

        # we have to check the overlapping intervals. So lets keep a array where overlapping array will be kept

        overlapping_arrays = []

    # Now we loop through the intervals. We know intervals has [start, end] 0 and 1 position
        
        for interval in intervals:   

            # First we check if the overlapping_arrays array is empty if it is empty then add the first interval.  if not empty then go with the  or  statement
            
            # The second statement checks the  most recent added overlapping_arrays values represented by [-1]  and check its 2nd element represented by [1].  Now check if the interval's first index is greater then the overlapping arrays last index if yes then array are not overlapping if  it is not greater than array is overlapping.

            if not overlapping_arrays or overlapping_arrays[-1][1] < interval[0]:
                
                overlapping_arrays.append(interval)
            else:
                # Here overlapping arrays falls 
                # In here, for e.g. [1,3] is already in array so to add the overlapping array of this we can add the second maximum element between this array and interval's second index interval[1]  for e.g if already [1,3] then for [2,6] the max of 3 and 6 i.e. 6 is added.  
                
                overlapping_arrays[-1][1] = max(overlapping_arrays[-1][1], interval[1])
            
        return overlapping_arrays

answer = Solution()
list= [[1,3],[2,6],[8,10],[15,18]]
output = answer.merge(list)

print(output)
"""


                 