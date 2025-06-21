
"""
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

"""
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)



"""
Explanation:

Outer Loop (for i in range(n)):
This loop controls the number of passes. In each pass, the largest unsorted element "bubbles up" to its correct position at the end of the unsorted portion of the array. The n - i - 1 in the inner loop ensures that elements already sorted are not re-evaluated.

Inner Loop (for j in range(0, n - i - 1)):
This loop iterates through the unsorted portion of the array, comparing adjacent elements.

Comparison and Swap (if arr[j] > arr[j + 1]:):
If the current element (arr[j]) is greater than the next element (arr[j + 1]), they are swapped to maintain ascending order. Python's tuple assignment arr[j], arr[j + 1] = arr[j + 1], arr[j] provides a concise way to perform the swap.
"""

"""
Optimization (Optional):
An optimization can be added to stop the sorting early if no swaps are made in a pass, indicating that the array is already sorted.
"""
def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to track if any swaps occurred in this pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr
    
# Example usage:
my_list_2 = [64, 25, 12, 22, 11]
optimized_sorted_list = bubble_sort_optimized(my_list)


print(f"Optimized list: {optimized_sorted_list}")

    