"""
Longest Substring Without Repeating Characters

Given a string, S. Find the length of the longest substring without repeating characters.

Example 1
Input : S = "abcddabac"
Output : 4
Explanation : The answer is "abcd" , with a length of 4.

Example 2
Input : S = "aaabbbccc"
Output : 2
Explanation : The answers are "ab" , "bc". Both have maximum length 2.
"""

class Solution:
    def longestNonRepeatingSubstring(self, s):
        #your code goes here
        seen = set()
        max_length = 0
        cur_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            cur_length = right -left + 1
            max_length = max(max_length, cur_length)
        return max_length
obj = Solution()
print(obj.longestNonRepeatingSubstring("abcdedabac"))