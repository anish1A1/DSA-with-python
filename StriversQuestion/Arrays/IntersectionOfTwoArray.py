

"""
Intersection of two sorted arrays
100
Easy
Hint
Given two sorted arrays nums1 and nums2, return an array that contains the intersection of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Examples:
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2]
"""



def intersection_of_arrays(arr1, arr2):
    i, j = 0, 0
    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # Avoid adding duplicates
            if not intersection or intersection[-1] != arr1[i]:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection

arr = [1, 2, 3, 4, 5, 6, 8, 8]
arr2 = [3, 5, 7, 8, 9, 9]

print(f"Intersection of arrays: {intersection_of_arrays(arr, arr2)}")

