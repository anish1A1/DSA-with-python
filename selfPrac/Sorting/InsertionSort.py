

def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        current_element = arr[i]
        j = i-1

        while j>=0 and arr[j] > current_element:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = current_element
    return arr

print(insertion_sort([9,16,6,26,0]))
        