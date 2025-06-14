"""
Check if array is sorted in descending order
"""

def arrInDesc(arr, n):
    
    if n == 1:
        return True
    if arr[n-1] > arr[n-2]:
        return False
    
     
    return arrInDesc(arr, n-1)


def arrInDescItr(arr, n):
   
    for i in range(n - 1):   
        if arr[i] < arr[i+1]:
            return False
    return True

n = [9, 7, 5, 3, 1]

print(f"\nArray in Recursive Approach :{arrInDesc(n, len(n))}") 

print(f"\nArray in Iterative Approach :{arrInDescItr(n, len(n))}") 