# Max Sum Subarray of size k

def max_sum_subbarray(nums, k):
    
    window_sum = 0
    max_sum = float('-inf')
    left =0
    
    for right in range(len(nums)):
        
        window_sum += nums[right]    
        
        if right - left + 1 ==k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left +=1
    
    return max_sum

print(max_sum_subbarray([1,2,3,3,2,1,6], 2))       