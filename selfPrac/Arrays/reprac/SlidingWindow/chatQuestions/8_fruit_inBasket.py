"""
Problem Statement
You are given an array of integers fruits where each integer represents a type of fruit.
You have two baskets, and each basket can only hold one type of fruit.
You want to pick as many fruits as possible in a row (contiguous subarray), but you can only carry at most two distinct types.

Return the maximum number of fruits you can pick.

Example 1
Code
Input: fruits = [1,2,1]
Output: 3
Explanation: You can pick all fruits → [1,2,1].
Example 2
Code
Input: fruits = [0,1,2,2]
Output: 3
Explanation: Pick [1,2,2].
Example 3
Code
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: Pick [2,3,2,2].
"""

from collections import defaultdict
def fruit_in_basket(fruits):
    max_fruit_picked = 0
    left = 0
    fruit_count = defaultdict(int)
    
    for right in range(len(fruits)):
        fruit_count[fruits[right]] += 1
        
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        max_fruit_picked = max(max_fruit_picked, right-left + 1)
    return max_fruit_picked

print(fruit_in_basket( fruits = [0,1,2,2]))
        
        
    