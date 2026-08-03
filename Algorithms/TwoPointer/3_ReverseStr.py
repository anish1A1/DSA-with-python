"""
 Problem Statement
Write a function that reverses a string.
The input string is given as an array of characters s.
You must do this in‑place (modify the array directly) with O(1) extra space.

Example
Code
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def rev_str(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        
        left += 1
        right -= 1
    return s
print(rev_str(["h","e","l","l","o"]))

