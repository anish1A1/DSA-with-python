
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
            


def merge_arrays(nums1, m, num2, n):
    left = 0
    right = (m + n) - 1
    i = m - 1
    j = n - 1
    k = m + n - 1 
    
    while i>= 0 and j>= 0:
        if nums1[i] > num2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else: 
            nums1[k] = num2[j]
            j-= 1
        k -= 1
        
    while j >= 0:
        nums1[k] = num2[j]
        k -= 1
        j -= 1
    return nums1

print(merge_arrays( nums1 = [1,2,3,0,0,0], m= 3, num2 = [2,5,6], n= 3))


# retrying the sorting array while merging from another array.

def re_merge_array(nums1, m, nums2, n):
    i = m -1
    j = n - 1
    total_length = m + n -1
    
    while i >=0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[total_length] = nums1[i]
            i -= 1
        else:
            nums1[total_length] = nums2[j]
            j -= 1
        total_length -= 1
    while j>=0 :
        nums1[total_length] = nums2[j]
        j -= 1
        total_length -= 1
    return nums1

print(re_merge_array( nums1 = [1,2,3,0,0,0, 0], m= 3, nums2 = [1, 2,5,6], n= 4))

# Dutch national flag

def dutchNational(nums):
    length = len(nums)
    start = 0
    end = length - 1
    middle_pointer = 0
    
    while middle_pointer <= end:
        if nums[middle_pointer] == 0:
            nums[start], nums[middle_pointer] = nums[middle_pointer], nums[start]
            
            start += 1
            middle_pointer += 1
        
        elif nums[middle_pointer] == 2:
            nums[end], nums[middle_pointer] = nums[middle_pointer], nums[end]
            
            end -= 1
            middle_pointer += 1
        
        else:
            middle_pointer += 1
    
    return nums

print(dutchNational(nums = [2,0,2,1,1,0]))
print(dutchNational(nums = [2,0,1]))


# repratice again of this 0, 1,2 

def checkFlagColour(nums):
    start = 0
    end = len(nums) - 1
    middle= 0
    
    while middle <= end:
        if nums[middle] == 0:
            nums[start], nums[middle] = nums[middle], nums[start]
            start += 1
            middle += 1
        elif nums[middle] == 2:
            nums[end], nums[middle] = nums[middle], nums[end]
            end -= 1
            middle += 1
        else:
            middle += 1
    return nums

print(checkFlagColour(nums = [2,0,2,1,1,0]))
print(checkFlagColour(nums = [2,0,1]))
            