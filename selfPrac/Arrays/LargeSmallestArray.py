

# Average case 
def Large_Small(arr):
    if len(arr) <= 0:
        return -1
    arr.sort()
    new_set = set(arr)
    new_list = list(new_set)
    if new_list[0] == new_list[-1]:
        return -1 
    
    small = new_list[0]
    lar = new_list[-1]
    
    return [small, lar]        

print(Large_Small([1,2,4,7,7,5]))


def Large_Small_Bst(arr):
    min = arr[0]
    max = arr[0]
    if len(arr) <= 1:
        return -1
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]
            
    if min == max:
        return -1
    return [min, max]
print(Large_Small_Bst([1,1,2,4,7,7,5,9]))
