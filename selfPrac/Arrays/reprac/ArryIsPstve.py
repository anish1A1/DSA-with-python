"""
Check if all elements in array are positive

"""

def CheckPositive(nums): 
    
    for i in nums:
        if i < 0:
            return "The array's elements contains negative"
        
    return "The array contains positive element"

print("\n",CheckPositive([2,-1,5,6]))