# to print the second largest but catch there can be 
# duplicate values too

"""
nums = [3,5,1,6,6]   this is the type of array we get
Now from here find the second largest

catch -> it will become [1,3,5,6,6] but the second last index ( 6 ) is not second largest it is 5


"""

def secondLargest(arr):
    
    # We 
    if len(arr) < 2:
        return -1  # 1 index doesnot have second largest
    
    largest = s_largest = float('-inf')   #Made float of minus infinity
    # largest = -infinity
    # second_largest = -infinity
    
    
    """
    hen for each number:
    - If it's greater than the largest, it becomes the new largest, and the old largest becomes the second largest.
    - If it’s in between largest and second largest, then it becomes the new second largest.

    """
    for num in arr:
        if num > largest:
            s_largest = largest
            largest = num
        
        elif largest > num > s_largest:
            s_largest = num
    
    return s_largest if s_largest != float('-inf') else -1

            
        
    
    
nums = [3,5,1,6,6,6] 

print(secondLargest(nums))