
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

#Reverse String
def revString(s):
    left = 0
    right = len(s) - 1
    
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -=1 
    return s
print(revString(["h","e","l","l","o"]))

def rem_dup(nums):
    if not nums:
        return 0
    left = 1
    
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left +=1 
    return nums[:left]
print(rem_dup([1,1,2]))
print(rem_dup([0,0,0,1,1,1,2,2,3,3,4]))


# again 

def removeDupli(nums):
    left = 1
    
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return nums[:left]
print(removeDupli([1,1,2]))
print(removeDupli([0,0,0,1,1,1,2,2,3,3,4]))

def move_zero(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    
    for i in range(left, len(nums)):
        nums[i] = 0
    return nums

print(move_zero([0,1,0,3,12]))

# Remove all instance of val in place and return the new length

def removeVal(nums, val):
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
        
    return left 
print(removeVal(nums = [3,2,2,3,2, 2, 3], val = 3))
            
