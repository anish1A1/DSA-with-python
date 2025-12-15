"""
Longest Substring With At Most K Distinct Characters

Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.

Example 1
Input : s = "aababbcaacc" , k = 2
Output : 6

Explanation : The longest substring with at most two distinct characters is "aababb".
The length of the string 6.

Example 2
Input : s = "abcddefg" , k = 3
Output : 4

Explanation : The longest substring with at most three distinct characters is "bcdd".
The length of the string 4.
"""
from collections import defaultdict
def LongestSubstr_atK_most(s, k):
    
    str_count = defaultdict(int)  #to store count of str
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        str_count[s[right]] += 1
        
        while len(str_count) > k:
            str_count[s[left]] -= 1 #remove first left elements
            
            if str_count[s[left]] == 0:
                del str_count[s[left]]
                #deleting key whose count is 0
            left+=1
        
        cur_count = right - left + 1
        max_length = max(max_length, cur_count)
        
    return max_length    

print(LongestSubstr_atK_most("abcddefg" , k = 3))

