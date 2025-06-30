"""
2124. Check if All A's Appears Before All B's

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
 

Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.

"""

def check_string(s):
    b_appered = False
    for num in s:
        if num == 'b':
            b_appered = True
        elif num == 'a' and b_appered:
            return False
    return True

print(check_string("aaabbb"))  #  True
print(check_string("abab"))    #  False

"""

###  Problem Insight:
You're given a string made only of `'a'` and `'b'` characters. You need to check if **all the 'a's come before any 'b'**.

That means:
- ✅ `"aaabbb"` is fine.
- ❌ `"aba"` is not, because an `'a'` comes **after** a `'b'`.

---

### ✅ Optimal Approach

We **scan the string once** from left to right. If we **ever see an `'a'` after seeing a `'b'`**, that breaks the rule.

### ✔️ Python Code:
```python
def check_string(s):
    seen_b = False
    for char in s:
        if char == 'b':
            seen_b = True
        elif char == 'a' and seen_b:
            return False
    return True
```

### 💡 How It Works:
- We use a flag `seen_b` to remember if we've already passed a `'b'`.
- If we see an `'a'` **after** that, we return `False`—because that means `'a'` is coming after a `'b'`.

### 🧪 Test Cases:
```python
print(check_string("aaabbb"))  # ✅ True
print(check_string("abab"))    # ❌ False
print(check_string("bbb"))     # ✅ True
print(check_string("aaa"))     # ✅ True
print(check_string("ba"))      # ❌ False
```

---

Let me know if you’d like a version using regex or if you want to try writing it recursively for fun.

"""