"""
5. Fruits Into Baskets (LeetCode 904)

Difficulty: Medium

Problem

You are given an array fruits.
You can pick at most two types of fruits.
Return the maximum number of fruits you can pick.

Example
Input: fruits = [1,2,1]
Output: 3
Explanation: Pick fruits of type 1 and 2.
"""
from collections import defaultdict

def fruit_pick_2(arr):
    seen = defaultdict(int)
    left = 0
    max_length = 0
    
    for right in range(len(arr)):
        seen[arr[right]] += 1
        
        while len(seen) > 2:
            seen[arr[left]] -= 1
            if seen[arr[left]] == 0:
                del seen[arr[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(fruit_pick_2([1,2,1]))
print(fruit_pick_2([1,2,1,2,1]))
print(fruit_pick_2([1,2,1,3,3,1]))


        