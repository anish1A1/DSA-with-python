# Problem 3: Minimum Window Substring
# Problem Statement:  

# Given two strings s and t, return the minimum window substring of s that contains all the characters of t. If no such substring exists, return an empty string.

# Example:

# Code
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Constraints:

# 1 ≤ s.length, t.length ≤ 10^5

# s and t consist of uppercase and lowercase English letters.



from collections import Counter
def min_window(s: str, t: str) -> str:
    
    if not s or not t:
        return ""
    
    left = 0
    needed = Counter(t)  #what we need
    window = Counter()   #what we have in current window
    have = 0
    need = len(needed)  #how many chars statisfied
    result_length = float('inf')
    result = ""
    
    for right in range(len(s)):
        window[s[right]] += 1
        
        # check if this char now satisfies requirement.
        if s[right] in  needed and window[s[right]] == needed[s[right]] :
            have += 1
        
        # shrink window when valid
        while have == need:
            # update result if smaller
            if (right - left + 1) < result_length:
                result_length = right - left + 1
                result = s[left:right+1]

            # shrink from left
            window[s[left]] -=1
            if s[left] in needed and window[s[left]] < needed[s[left]]:
                have -=1
            left +=1
        
    return result
    
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s,t))