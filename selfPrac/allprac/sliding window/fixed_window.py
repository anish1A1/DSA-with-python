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

print('\n')
# problem 2: average of subarray size k'

def avg_size_k(arr, k):
    
    current_sum = sum(arr[:k])
    # print(current_sum)
    
    max_average = current_sum / float(k)
    
    for i in range(k, len(arr)):
        current_sum += arr[i]
        current_sum -= arr[i-k]
        
        average = current_sum / float(k)
        max_average = max(max_average, average)
    return max_average

print(avg_size_k([1,12,-5,-6,50,3], 4))


# Retry Max average of size k

def average_size_k(arr, k):
    current_sum = sum(arr[:k])
    max_average = current_sum / float(k)
    
    for i in range(k, len(arr)):
        current_sum += arr[i]
        current_sum -= arr[i - k]
        
        average = current_sum / float(k)
        max_average = max(average, max_average)
        
    return max_average
print(average_size_k([1,12,-5,-6,50,3], 4))
 