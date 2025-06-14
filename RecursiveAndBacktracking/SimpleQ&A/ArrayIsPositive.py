"""
Check if all elements in array are positive

"""


def checkPos(arr, n):
    if n == 0 or n == 1:
        return True
    
    if arr[n-1] < 0:   #python index start from zero, and we used length as n value. but the total numbers of arr for [-1,4,56,4]  is 4 as list start from 0.
        #So we use n-1  (imp) otherwise index out of bound error.
        return False
    
    return checkPos(arr, n-1)


arr = [-1,4,56,4]
print(f"It has negative num. : {checkPos(arr, len(arr))}")