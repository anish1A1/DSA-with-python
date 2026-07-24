"""
Longest Substring with K Distinct Characters
- Problem: Given a string, find the length of the longest substring that contains at most k distinct characters.

- Example:
- Input: s = "araaci", k = 2
- Output: 4 (substring "araa")

"""

from collections import defaultdict

def KDistinctCharacter(nums, k):
    left = 0
    char_count = defaultdict(int)
    max_length = 0
    
    for right in range(len(nums)):
        char_count[nums[right]] +=1
        
        while len(char_count) > k:
            char_count[nums[left]] -= 1
            if char_count[nums[left]] == 0:
                del char_count[nums[left]]
            left+=1
            
        max_length = max(max_length, right - left + 1)
    return max_length

k = 2
print(KDistinctCharacter('araaci',k))
    
    