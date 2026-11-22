# longest substring without repeating character

def long_subs_ubnique(s):
    seen = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1 
        
        seen.add(s[right])
        current_length = right - left + 1
        max_length = max(current_length, max_length)
    return max_length

print(long_subs_ubnique('abcabcbb'))


# Longest substring at Most K Distinct characters

from collections import defaultdict
def long_substr(s, k):
    seen = defaultdict(int)
    left = 0
    window_length = 0
    max_length = 0
    
    if k==0 or not s:
        return 0
    for right in range(len(s)):
        seen[s[right]] += 1
        
        while len(seen) > k:
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1
            
        window_length = right -left + 1
        max_length = max(window_length, max_length)
    return max_length

print(long_substr(s="abcddefg" , k = 3))
        