"""
Problem Statement
Given a string s, find the length of the longest substring without repeating characters.

Example 1
Code
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length = 3.
Example 2
Code
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with length = 1.
Example 3
Code
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length = 3.
"""

def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    longest_substr = 0
    
    for right in range(len(s)):
        
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        current_window_size = right - left + 1
        longest_substr = max(longest_substr, current_window_size)
    
    return longest_substr

print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))     # 1
print(lengthOfLongestSubstring("pwwkew"))    # 3