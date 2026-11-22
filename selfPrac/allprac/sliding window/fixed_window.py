# Max Sum

def Max_sum_subarray_size_k(arr, k):
    left = 0
    window_sum = 0
    max_sum = float('-inf')

    for right in range(len(arr)):
        window_sum += arr[right]
        
        if right - left + 1 == k:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[left]
            left +=1 
            
    return max_sum   
print(Max_sum_subarray_size_k([1,2,3,4,5,6], 3))

# problem 2 