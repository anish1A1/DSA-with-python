"""
From a given array [1,2,7,9,35] find value 9 and return its index
 
"""

"""
Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

"""

# Using recursive way:
def binarySerach(arr, start, end , target):
    if start <= end:
        mid = end + (start - end) //2  #
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return binarySerach(arr, mid +1, end, target)
        else:
            return binarySerach(arr, start, mid -1, target)
    else:
        return -1
    
    
#Using Iterative way

def binarySerachIttr(arr, start, end, target):
    while end >= start:
        mid = end + (start -end) //2
        
        #if x is present at mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:  # if target is bigger than start from mid + 1 and ignore left half
            
            # for e.g if index 3 =7 and is  7 > 5  then start from 3+1 = 4th index 
            start = mid + 1
        else:  # if target is smaller, ignore right half
            end = mid -1
            
    # If we reach here, then the element
    # was not present
    return -1



if __name__ == "__main__":
    arr = [1,2,7,9,35]
    start =0
    end = len(arr) -1
    target = 35
    
    print(f"\nThe value 9 index is  {binarySerach(arr, start, end, target)}\n")
    print(f"\nThe value 9 index is  {binarySerachIttr(arr, start, end, target)}\n")