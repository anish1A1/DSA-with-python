"""
1456. Maximum Number of Vowels in a Substring of Given Length
Medium

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""
# Hint: it just like max average of size k problem.

def vowel_in_size_k(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    vowel_count = 0
    for i in range(k):
        if s[i] in vowels:
            vowel_count += 1
    
    max_vowel_count = vowel_count
    
    for i in range(k, len(s)):
        if s[i] in vowels:
            vowel_count += 1
        if s[i-k] in vowels:
            vowel_count -= 1
        
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
        
        # optimization if the vowel is equal to k length then max answer already found break loop.
        
        if max_vowel_count == k:
            return k
    
    return max_vowel_count

print(vowel_in_size_k(s = "abciiidef", k = 3))
print(vowel_in_size_k(s = "aeiou", k = 2))
print(vowel_in_size_k(s = "leetcode", k = 3))

