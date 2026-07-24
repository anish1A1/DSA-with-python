"""
Title: Maximum Number of Vowels in a Substring of Given Length

Problem Statement:  
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowels are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Code
Input: s = "abciiidef", k = 3
Output: 3
Explanation: Substring "iii" contains 3 vowels.
Example 2:

Code
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Code
Input: s = "leetcode", k = 3
Output: 2
Explanation: Substring "lee" contains 2 vowels.
Constraints:

1 ≤ s.length ≤ 10⁵

s consists of lowercase English letters.

1 ≤ k ≤ s.length
"""

from collections import defaultdict

def max_num_of_vowel_ink(s, k):
    vowels = 'aeiou'
    count = 0
    
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count
        
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        
        # before counting the new index and max count, first remove the previous index  and make the window of size k
        
        if s[i-k] in vowels:
            count -= 1
        max_count = max(max_count, count)   
    
    return max_count 

print(max_num_of_vowel_ink(s = "leeetcode", k = 3))