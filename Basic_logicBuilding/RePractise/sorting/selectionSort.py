


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
