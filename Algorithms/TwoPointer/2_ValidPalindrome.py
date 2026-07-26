"""
Problem Statement
Given a string s, return True if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Otherwise, return False.

Example 1
Code
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2
Code
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.
"""

def palindromeCheck(s):
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        #skip non-alpha numeric
        while left < right and not s[left].isalnum():
            left += 1 
        
        while left < right and not s[right].isalnum():
            right -= 1
        
        # compare ignoring cases 
        if s[left].lower() != s[right].lower():
            return False 
        
        left+=1
        right-=1
    return True
print(palindromeCheck("A man, a plan, a canal: Panama"))
print(palindromeCheck("race a car"))


"""
left < right and not s[left].isalnum()
will check if left is less than right and the s[left] is not alpha numeric.
when it is not alpha numeric (for e..g it is !, : , spaces " "), then
increase the left pointer 
left +=1

like wise with s[left] too
"""
