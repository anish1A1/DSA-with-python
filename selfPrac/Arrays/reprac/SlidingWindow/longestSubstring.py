# longest substring without repeating character.
# [abcabcbb]  here only unique needed abc only.


def longest_substr_unique(s):
    
    max_length = 0
    seen = set()
    left = 0
    for right in range(len(s)):
    
        while s[right] in seen:
            seen.remove(s[left])
            print("When removing ", seen)
            left += 1

        seen.add(s[right])
        print("When adding ",seen)
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return f"Max length is {max_length}"

print(longest_substr_unique('abcabcbb'))
        