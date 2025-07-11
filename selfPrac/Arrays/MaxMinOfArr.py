"""
Maximum and minimum of an array using minimum number of comparisons

Given an array, the task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Examples:

Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35
              
"""


def findMinMax(arr):
    if len(arr) == 1 :
        return arr
    
    min = arr[0]
    max = arr[0] 
    
    # for i in range(len(arr)):
    #     pass
    
    for num in arr:
        if num >= max:
            max = num  
        elif num <= min:
            min = num
    return [min, max]

arr = [22, 14, 8, 17, 35, 3]
minMax = findMinMax(arr)
print(minMax)



def findMinMaxPointer(arr):
    
    if len(arr) <=1:
        return arr
    
    i=0
    min = float('inf')
    max = float('-inf')
    
    while i < len(arr):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
        i+=1
    return [min,max]
print(findMinMaxPointer(arr))