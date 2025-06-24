
"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


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
    
    
    
"""
 How Backtracking Works Visually:

START dfs(0)
    include 1 ➜ subset = [1]
        dfs(1)
            include 2 ➜ subset = [1, 2]
                dfs(2)
                    include 3 ➜ subset = [1, 2, 3]
                        dfs(3) ➜ append [1, 2, 3]
                    exclude 3 ➜ backtrack ➜ subset = [1, 2]
                        dfs(3) ➜ append [1, 2]
            exclude 2 ➜ backtrack ➜ subset = [1]
                dfs(2)
                    include 3 ➜ subset = [1, 3]
                        dfs(3) ➜ append [1, 3]
                    exclude 3 ➜ backtrack ➜ subset = [1]
                        dfs(3) ➜ append [1]
exclude 1 ➜ backtrack ➜ subset = []
    dfs(1)
        include 2 ➜ subset = [2]
            dfs(2)
                include 3 ➜ subset = [2, 3]
                    dfs(3) ➜ append [2, 3]
                exclude 3 ➜ backtrack ➜ subset = [2]
                    dfs(3) ➜ append [2]
        exclude 2 ➜ backtrack ➜ subset = []
            dfs(2)
                include 3 ➜ subset = [3]
                    dfs(3) ➜ append [3]
                exclude 3 ➜ backtrack ➜ subset = []
                    dfs(3) ➜ append []
    
    
"""