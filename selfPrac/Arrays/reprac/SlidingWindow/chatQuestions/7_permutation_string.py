"""
Problem Statement
Given two strings s1 and s2, return True if s2 contains a permutation of s1.
In other words, return True if one of s1’s permutations is a substring of s2.

Example 1
Code
Input: s1 = "ab", s2 = "eidbaooo"
Output: True
Explanation: s2 contains "ba", which is a permutation of "ab".
Example 2
Code
Input: s1 = "ab", s2 = "eidboaoo"
Output: False

"""

from collections import defaultdict, Counter

def permutation(s1, s2):
    left = 0
    char_check = Counter()
    s1_counter = Counter(s1)
    
    for right in range(len(s2)):
        char_check[s2[right]] += 1
        
        while right - left + 1 > len(s1):
            char_check[s2[left]] -= 1
            
            if char_check[s2[left]] == 0:
                del char_check[s2[left]]
            left += 1
        if char_check == s1_counter:
            return True
    return False

print(permutation(s1 = "ab", s2 = "eidboaoo"))
        
    
    