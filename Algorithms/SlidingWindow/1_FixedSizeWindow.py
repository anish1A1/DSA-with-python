# “Given an array, find something in subarrays of size k”


def fixed_window(arr, k):
    left = 0
    window_sum= 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        print(f"Current sum {window_sum}")
        
        if right - left + 1 == k:
            window_sum -= arr[left]
            print(f"Reducing the left pointer index value {arr[left]}, now the sum is {window_sum}")
            left += 1
    
    return window_sum

print(fixed_window([1,2,3,4,5,6,7,8,9], 3))            


# Here we add the sum first, then when the, current position - left pointer position + 1 == k(the subbarry of size k)

# We remove the array's left pointer index from the window_sum 
# Then we increase the left pointer index.
# It keeps on repeating

"""
For example: k=3 & arr= [1,2,3,4,5,6,7,8,9], sum=?:

Current sum 1
Current sum 3
Current sum 6  (untill right pointer index = 2)

# Now the right pointer index = 2,  left pointer value = 0, and k=3.

# So, 2(right)-0(left) +1 = 3  , and k= 3. That means we need to stop and remove the left pointer value from array i.e. arr[left] (arr[0]) == 1, from the current_sum
# Now the current sum is 
Reducing the left pointer index value 1, now the sum is 5.  since, [2+3(1 value is removed)]

# We also added +=1 in the left pointer, so when iterating sum will be,
Current sum 9    since, [5+4]

Reducing the left pointer index value 2, now the sum is 7
Current sum 12
Reducing the left pointer index value 3, now the sum is 9
Current sum 15
Reducing the left pointer index value 4, now the sum is 11
Current sum 18
Reducing the left pointer index value 5, now the sum is 13
Current sum 21
Reducing the left pointer index value 6, now the sum is 15
Current sum 24
Reducing the left pointer index value 7, now the sum is 17
17
"""
