"""
4. Longest Substring Without Repeating Characters
- Problem: Given a string, find the length of the longest substring without repeating characters.

- Example:
- Input: s = "abcabcbb"
- Output: 3 (substring "abc")

"""

def non_repeating_Substr(s):
    seen = set()
    left =0
    max_length = 0
    window_length = 0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        window_length = right - left + 1
        max_length = max(max_length, window_length)
    return max_length
print(non_repeating_Substr(s = "abcabcbb"))