
# Selection Sort means to select an lowest value element and sort it first 

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        current_index = i
        for j in range(i+1, n):
            if arr[j] < arr[current_index]:
                current_index = j
            
        arr[i], arr[current_index] = arr[current_index], arr[i]
    return arr

print(selection_sort([9,16,6,26,0])) 