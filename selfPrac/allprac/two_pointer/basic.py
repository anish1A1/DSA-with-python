
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sums = nums[left] + nums[right]
        
        if sums == target:
            return [left + 1, right + 1]
        elif sums < target:
            left += 1
        else:
            right -= 1
    return 0, 0
print(twoSum([2,7,11,15], target = 9))\
    
# PalinDrome

def palindromeCheck(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
print(palindromeCheck("A man, a plan, a canal: Panama"))
print(palindromeCheck("race a car"))

def revString(s):
    left = 0
    right = len(s) - 1
    
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -=1 
    return s
print(revString(["h","e","l","l","o"]))