"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def check_paranthesis(s: str):
    stack = []
    check_closed_par = {
        ')':'(',
        '}' : '{',
        ']': '['
        }
    
    for cur_bracket in s:
        if cur_bracket in check_closed_par.values():    #opening bracket  #1
            stack.append(cur_bracket)
    
        else:       #closing bracket  #2
            if not stack:    #3
                return False
            if stack[-1] != check_closed_par[cur_bracket]:   #4
                return False
            # remove the last added element 
            stack.pop()      #5
                
    return not stack    #6
            

s = "([)]"
s1 ="()[]{}"

print(check_paranthesis(s =s))
print(check_paranthesis(s =s1))
