# Example: Max Sum Subarray of Size K


def Max_subarry_sizeK(arr, k):
    left = 0
    window_sum = 0
    max_sum = float('-inf')
    
    for right_pointer in range(len(arr)):
        window_sum += arr[right_pointer]
        
        if right_pointer - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            print(f"Maximum Subarray of {left}th Subarry is {max_sum}")
            window_sum -= arr[left]
            left += 1
            
    return f"The Maximum value of a single Subarray is {max_sum}."

print(Max_subarry_sizeK([1,2,3,4,5,6], 3))