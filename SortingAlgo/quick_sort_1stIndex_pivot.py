

def partition(arr, low, high):
    
    pivot = arr[low]
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low] 
    return i - 1


def quick_sort(arr, low , high):
    if high > low:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi -1)
        quick_sort(arr, pi + 1, high)
    
    

data = [1, 7, 4, 1, 10, 9, 2]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

# If we call this in a function then in the quick_sort function in the end write this line --> return arr


print('Sorted Array in Ascending Order:')
print(data)


"""
def partition(array, low, high):
    pivot = array[low]  # 1️⃣ Pick the first element as the pivot
    i = low + 1         #2️⃣ Start comparing from the next element

    for j in range(low + 1, high + 1):  # 3️⃣ Iterate through the rest of the subarray
        if array[j] < pivot:            # 4️⃣ If current element is smaller than pivot
            array[i], array[j] = array[j], array[i]  # 5️⃣ Swap it to the left side
            i += 1                      # 6️⃣ Move the boundary forward

    array[low], array[i - 1] = array[i - 1], array[low]  # 7️⃣ Place pivot in correct position
    return i - 1  # 8️⃣ Return pivot’s new index

def quick_sort(array, low, high):
    if low < high:  # 9️⃣ Base case check
        pi = partition(array, low, high)  # 🔟 Partition the array
        quick_sort(array, low, pi - 1)    # 1️⃣1️⃣ Recursively sort left part
        quick_sort(array, pi + 1, high)   # 1️⃣2️⃣ Recursively sort right part

"""

