

def merge(arr):
    if len(arr) <=1:
        return arr 
    
    mid = len(arr) // 2
    
    left_half = merge(arr[:mid])
    right_half = merge(arr[mid:])
    
    return arr_merge(left_half, right_half)

def arr_merge(left_half, right_half):
    result = []
    i=j=0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i+=1
        else:
            result.append(right_half[j])
            j+=1
    
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result

print(merge([54,26,93,17,77,31,44,55]))