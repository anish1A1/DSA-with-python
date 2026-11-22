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