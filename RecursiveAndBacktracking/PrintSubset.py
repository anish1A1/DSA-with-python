
"""
To print all the subsets for a given array

if there is [1,2,3]
then find its subset, tip : 2^n  where n is the no. of items in the array.

ans should be like [1,2,3], [1,2], [1,3], [], ...
a total of 8 
"""

def printSubset(arr):
    result = [] # To store the final list of all subsets
    subset = []
    
    def dfs(i):
        if i >= len(arr):
            return result.append(subset.copy())
        
        # decision to include arr[i]
        subset.append(arr[i])
        dfs(i+1)
        
        # decision to NOT add arr[i]
        subset.pop()
        dfs(i+1)
        
    dfs(0)   #start from index 0 which is array val 1.
    return result

print(f"{printSubset([1,2,3])}")
    
    