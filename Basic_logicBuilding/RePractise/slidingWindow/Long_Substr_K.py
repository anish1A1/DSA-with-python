"""
Longest Substring with K Distinct Characters
- Problem: Given a string, find the length of the longest substring that contains at most k distinct characters.

- Example:
- Input: s = "araaci", k = 2
- Output: 4 (substring "araa")

"""

def long_substr_k_char(s, k):
    curr_length = 0
    max_length = 0 
    seen = set()
    left = 0
    
    for right in range(len(s)):
        while s[right] in seen and len(seen) == k:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        curr_length = right - left + 1
        max_length = max(curr_length, max_length)
    return max_length

print(long_substr_k_char(s = "araaci", k = 2))
        
        
        