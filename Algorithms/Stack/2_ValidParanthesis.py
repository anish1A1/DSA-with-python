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
print('\n')


def check_paranthesis_again(s: str):
    stack = []
    
   
    pairs =  {
            ')':'(',
            '}' : '{',
            ']': '['
            }

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack) == 0

s = "([)]"
s1 ="()[]{}"

print(check_paranthesis_again(s =s))
print(check_paranthesis_again(s =s1))



"""
We are using a stack (Last in First out)

We add the elements and when we find the [-1] element key equals to current value. then pop it else return False because the elements did not work on correct order of closing the paranthesis.

Explanation of Each Numbered Line
#1 → Opening bracket check

check_closed_par.values() are '(', '{', '['.
If the current character is one of those, it’s an opening bracket.
Push it onto the stack because we’re waiting for a matching closing bracket later.

 #2 → Closing bracket case

If the current character is not an opening bracket, it must be a closing bracket (')', '}', ']').
Now we need to check if it matches the most recent opening bracket stored in the stack.


#3 → if not stack
This checks if the stack is empty when we encounter a closing barcket.
If the stack is empty, it means there is no opening bracket to match this closing one --> Invalid string.
Example ")(" --> the very first ")" has no opening before it so return False

#4 → Matching check

stack[-1] is the top of the stack (the most recent opening bracket).
check_closed_par[cur_bracket] gives the expected opening bracket for this closing one.

Example: if cur_bracket = ')', then check_closed_par[')'] = '('.

If they don’t match, the parentheses are invalid.

Example: "([)]" → when you see ), the top of stack is [, but ) expects ( → mismatch.


#5 → Pop the matched opening bracket
If the closing bracket matched correctly, remove the opening bracket from the stack.

This means that pair is complete and balanced.

#6 → Final check

After processing the whole string, return not stack.

If the stack is empty → all brackets matched correctly → return True.

If the stack still has items → some opening brackets never got closed → return False.

✅ Why if not stack: return False is Needed
Because you can’t pop from an empty stack.

More importantly, it prevents cases where a closing bracket appears without a corresponding opening bracket.

Example: "())" → when the second ) comes, the stack is empty, so we immediately return False.
"""