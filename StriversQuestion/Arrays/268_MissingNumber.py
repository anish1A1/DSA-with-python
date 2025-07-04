
"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array. 

Example 1:

Input: nums = [3,0,1]
Output: 2

Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2

Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 
"""


def findMissing_WorstApproach(arr):
    
    n = len(arr)
    
    for i in range(n + 1):
         
        if i not in arr:
            return i
    # TC = 0(n2)  and  SC = 0(1) 

# Here we know that if len(arr) = 5, then there length = 6, since 1 array is missing.  Now we loop again till end of the arr to check the missing number in this array and return the missing. 



def findMissing_AverageApprach(arr):
    n = len(arr)
    arr.sort()
    
    for i in range(n):
        if i != arr[i]:
            return i
    
    return n
    # Sorting takes nlog(n)  so, TC is nlog(n)  and SC = o(1)
    
# Here we sorted the elements now for each index, the element will be equal to its index. If it does not found the missing element, then the last element is missing, returned the len(arr).


def FindMissing_Optimal(arr):
    n = len(arr)
    
    sum_of_actual_arr = n* (n + 1) //2               #math formula of sum. 
    
    sum_of_arr = sum(arr)
    
    return sum_of_actual_arr - sum_of_arr 

# We are using the sum formula 
# - Calculate what the sum should be for numbers 0..n.
# - Subtract actual sum → you're left with the missing number.
# - Elegant and very efficient!



nums = [3, 0, 1]
print(findMissing_WorstApproach(nums))  # Output: 2
print(findMissing_AverageApprach(nums)) 
print(FindMissing_Optimal(nums)) 
