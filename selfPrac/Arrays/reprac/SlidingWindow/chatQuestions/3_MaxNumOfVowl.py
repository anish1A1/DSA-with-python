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