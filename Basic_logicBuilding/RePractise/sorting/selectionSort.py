


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(f"Sorted list: {sorted_list}")

        
        

def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j+ 1] = arr[j+1], arr[j]
            swapped = True
            
        if not swapped:
            break
    return arr

# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(my_list)
print(f"Sorted list: {sorted_list}")


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        
        while j >=0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = current
    return arr


# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = insertion_sort(my_list)
print(f"Sorted list: {sorted_list}")



def insetion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        current = arr[i]
        j = i -1 
        
        while j > 0 and arr[j] > current :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr


# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(my_list)
print(f"Sorted list: {sorted_list}")





def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left_side = merge_sort(arr[:middle_index])
        
    right_side = merge_sort(arr[middle_index:])
    return merge(left_side, right_side)

def merge(left_side, right_side):

    result = []
    i=j = 0
    
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            result.append(left_side[i])
            i +=1
        else:
            result.append(right_side[j])
            j +=1
    
    result.extend(left_side[i:])
    result.extend(right_side[j:])
    
    return result



# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = merge_sort(my_list)
print(f"Sorted list: {sorted_list}")




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left , right):
    
    result = []
    i = j =0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1 
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = merge_sort(my_list)
print(f"Sorted list: {sorted_list}")





def quick_sort(arr, start, end):
        
    if start < end:
        
        middle_index = partition(arr, start, end)
        quick_sort(arr, start, middle_index - 1)
        quick_sort(arr, middle_index + 1, end)
        

def partition(arr, start , end):
    
    pivot = arr[end]
    i =  start - 1
    
    for j in range(start, end):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    
    return i+1

data2 = [1, 7, 4, 1, 10, 9, 2]
print("Unsorted Array")
print(data2)

size = len(data2)

quick_sort(data2, 0, size - 1)


print('Sorted Array in Ascending Order:')
print(data2)


