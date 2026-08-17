

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    
    for right in range(low + 1, high + 1):
        
        if arr[right] <= pivot:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
    # Swap the new pointers
    arr[low], arr[left - 1] = arr[left - 1], arr[low]
    return left - 1  
    #Returning the index of new pivot.
 

def quick_sort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quick_sort(arr, low, part - 1)
        quick_sort(arr, part + 1, high)
        
arr= [54,26,93,17,77,2,31,44,55]
print("Our array is: ", arr)
lengt = len(arr) - 1
quick_sort(arr, 0, lengt)

print("Sorted, In-place arr: ", arr)