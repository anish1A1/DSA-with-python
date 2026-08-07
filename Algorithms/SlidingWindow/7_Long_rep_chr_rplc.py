"""
424. Longest Repeating Character Replacement
Medium

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""
from collections import defaultdict
def characterReplacement(s, k):
    left = 0
    max_len = 0
    char_count_dict = defaultdict(int)
    max_freq = 0 #This will keep track of maximum value of a single character in dict.
    
    for right in range(len(s)):
        char_count_dict[s[right]] += 1
        max_freq = max(max_freq, char_count_dict[s[right]])
        # get the max frequency of most added character. (greater count)
        
        while (right - left + 1) - max_freq > k:
            char_count_dict[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    return max_len

print(characterReplacement(s = "ABAB", k = 2))


    # After that we will compare the max_freq of that char - the current sliding window length is greater than k (replacebale character count).

    # If its greater than k it means that,
    # dict = {A:3, B:2} (current),  and k = 2 
    # for now the value of max_freq = 3  (since 3 A's)

    # Now when go to next element, if the next element is again B, then    
    # dict = {A:3, B:3} (current); 
    # now cuurent length = 6, and max_freq = 3,
    # so  6- 3 = 3  i.e.  3 > k(2), we remove the first index value i.e. left, then it will be
    # dict = {A:2, B:3}  
    # since not more than 2 count of different should be greater than k(2).
    
    