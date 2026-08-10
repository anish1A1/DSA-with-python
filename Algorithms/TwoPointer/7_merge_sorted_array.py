"""
88. Merge Sorted Array
Solved
Easy

Hint
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

def merge_srted_arr(nums1, m, nums2, n):
    
    i = m-1  #getting the last index of all
    j = n-1
    last_index = m+n -1     #last index of m + n  with -1 to get index.
    
    while i>= 0 and j >= 0:     #since we are doing with index 0th index will also have value.
        if nums1[i] > nums2[j]:
            nums1[last_index] = nums1[i] 
            i -= 1
        else:
            nums1[last_index] = nums2[j]
            j -= 1
        last_index -=1   #last_index will be deducted in each loop because a element is changed in each loop.
    
    while j >= 0:
        nums1[last_index] = nums2[j]
        j -= 1
        last_index -=1
        
    return nums1 

print(merge_srted_arr( nums1 = [1,2,3,0,0,0], m= 3, nums2 = [2,5,6], n= 3))


"""

Problem Recap
You are given two sorted arrays:

nums1 of length m + n (first m elements valid, last n are placeholders 0).
nums2 of length n.
Merge nums2 into nums1 in non‑decreasing order.
Do it in‑place (no extra array).


Key Insight
If you merge from the front, you risk overwriting elements in nums1 that you still need.

Instead, merge from the back:
Start with the largest elements of both arrays.
Place them at the end of nums1.
Move pointers inward.

Correct Pointer Setup
i = m - 1 → last valid element in nums1.
j = n - 1 → last element in nums2.
k = m + n - 1 → last index of nums1 (where merged elements go).


Algorithm
While both arrays have elements (i >= 0 and j >= 0):

Compare nums1[i] and nums2[j].
Place the larger one at nums1[k].
Move the pointer (i or j) and decrement k.

If nums2 still has leftover elements, copy them into nums1.
(No need to copy leftovers from nums1 — they’re already in place.)


Example Walkthrough
Input:
nums1 = [1,2,3,0,0,0], m = 3  
nums2 = [2,5,6], n = 3

Steps:

Compare 3 vs 6 → place 6 at end.

Compare 3 vs 5 → place 5.

Compare 3 vs 2 → place 3.

Compare 2 vs 2 → place 2.

Copy remaining 2.

Output: [1,2,2,3,5,6]

Complexity
Time: O(m + n)

Space: O(1) (in‑place)

✅ Summary: You solved it by realizing the trick is to merge backwards using three pointers (i, j, k). This avoids overwriting and ensures the merge is done in‑place.


This is a classic two pointer approach where me use merger like merge sort. There are 0's in nums1 and we need to return num1 array too so, we need to modify the num1 list. 

The best approach is to use compare the list from the end of their list. i.e last index. We get the last element when adding m+n. now to get index deduct -1. Now we can easily compare the two index of both list with the help of m and n of both arrays. also deduct -1 to get index. We add the element which is greatest in the num1 with with the help of last index.


Here is a catch after the loop completes there the first element of any one of list whose element is smaller will remain. We also need to add it, since we are return nums1 if the lowest element is inside num1 then it is already added. Nums1[1,2] and num2[2,3] here result of loop will be [2,2,3]. since it was in nums1 it already has [1] so result is [1,2,2,3]. But for num2 if the smaller element is in it then, we need to add seperately, since n still is not 0 so do loop with n>0, then add the nums1[last] = nums2[n], then we also decrement n and last by 1. Then the result will be [1,2,2,3].
"""