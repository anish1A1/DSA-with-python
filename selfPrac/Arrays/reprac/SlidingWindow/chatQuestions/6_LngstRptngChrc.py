"""
Problem Statement
You are given a string s and an integer k.
Return the length of the longest substring that can be obtained by replacing at most k characters so that all characters in the substring are the same.

Example 1
Code
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with 'B's or vice versa → "BBBB" or "AAAA".
Example 2
Code
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'B' → "AABA" or "ABAA".


You want the length of the longest substring where you can change at most k characters so that the whole substring becomes the same letter.
"""

from collections import defaultdict
def lngst_rptng_chrc_atk(s, k):
    
    max_length = 0
    count = defaultdict(int)
    max_freq_of_a_charac = 0
    left = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        
        max_freq_of_a_charac = max(max_freq_of_a_charac, count[s[right]])
        
        
        while (right - left + 1) - max_freq_of_a_charac > k:
            count[s[left]] -= 1
            left  += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(lngst_rptng_chrc_atk(s = "AABABBA", k = 1)) 
print(lngst_rptng_chrc_atk(s = "ABAB", k = 2)) 

        


"""
 for e.g.  "AABABBA"  here when index is 5 then the while loop will start because current window has more than k different character.
 
 max freq will be 3 because A: 3 and B: 2 (window size = total 5)
 so, 5 + 1 (1 is always added sliding window) - 3(A max value) = 3
 
 i.e. 3 is greater than 2 (of K). Now the while loop starts.
  
"""
