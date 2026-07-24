"""
Title: Find All Anagrams in a String

Problem Statement:  
Given two strings s and p, return all the starting indices of p's anagrams in s.
You may return the answer in any order.

Example 1:

Code
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
The substring starting at index 0 ("cba") is an anagram of "abc".
The substring starting at index 6 ("bac") is also an anagram of "abc".
Example 2:

Code
Input: s = "ababc", p = "ab"
Output: [0, 1, 2]
Explanation:
Substrings "ab", "ba", and "ab" are all anagrams of "ab".
Constraints:

1 ≤ s.length, p.length ≤ 3 × 10⁴

s
"""

from typing import List
from collections import Counter

def findAnagrams(s: str, p: str) -> List[int]:
    
    p_values = Counter(p)    
    anagrams = []
    window_counter = Counter()
    len_p = len(p)
    
    
    for i, ch in enumerate(s):
        window_counter[ch] += 1    #count characters
        
        if i >= len_p:
            prev_value = s[i-len_p]
            window_counter[prev_value] -= 1
            
            if window_counter[prev_value] == 0:
                del window_counter[prev_value]
        
        if window_counter == p_values:
            anagrams.append(i - len_p + 1)
        
    return anagrams


        
print(findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print(findAnagrams("abab", "ab"))          # [0, 1, 2]