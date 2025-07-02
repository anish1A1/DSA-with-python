

def rotate(nums, k):
    k = k % len(nums)

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, len(nums) - 1)      # Step 1: reverse the whole array
    reverse(0, k - 1)              # Step 2: reverse first k elements
    reverse(k, len(nums) - 1)      # Step 3: reverse the rest
    
    return nums
    
    # for i in range()
    
nums = [1,2,3,4,5,6]
d =2
print(rotate(nums, d))



"""

Modulo Operation: First, calculate k % n to handle cases where k is larger than the length of the array. This ensures the rotation is within bounds.

for e.g n = 7 anbd k =3, Now when we divide the k with n, it will look like  3 % 7   so than means  7)3(   its ans. will be 3  since 3 is the remainder of this problem.
     

Reverse the Entire Array: Reverse the entire array to prepare for rotating.

Reverse the First Part: Reverse the first k elements to correctly place them in the rotated array.

Reverse the Remaining Part: Reverse the remaining elements (from index k to the end) to finalize the rotation.


➤ Step 1: Reverse the entire array
From: [1, 2, 3, 4, 5, 6, 7]
To: [7, 6, 5, 4, 3, 2, 1]
➤ Step 2: Reverse the first k = 3 elements
From: [7, 6, 5, 4, 3, 2, 1]
To: [5, 6, 7, 4, 3, 2, 1]
➤ Step 3: Reverse the remaining n - k elements
From: [5, 6, 7, 4, 3, 2, 1]
To: [5, 6, 7, 1, 2, 3, 4]
✅ Final result is the array rotated to the right by 3 steps.


"""

"""

        Here we will first take the remainder by k = k % n    for e.g 3 % 7 => 3,

        then make a swapper function which will swap start and end values
        after swapping the start and end indexes will increment and decrement respectively

        We will call swapper function three time 
        One to reverse all the array --> [1,2,3,4,5]  => [5,4,3,2,1]
        Then another to sort the array till k_th element--> [5,4,3,2,1] if k=2 then [5,4,1,2,3]
        Then another to sort the remaining array => [5,4,1,2,3]
"""