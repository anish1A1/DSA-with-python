"""
Selection Sort is a simple, comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part. This process continues until the entire list is sorted. 

Iterate through the list:
Start from the first element and iterate up to the second-to-last element. This outer loop defines the "sorted" and "unsorted" portions of the list.

Find the minimum element:
In each iteration of the outer loop, assume the current element is the minimum. Then, iterate through the remaining unsorted portion of the list to find the actual minimum element. Keep track of the index of this minimum element.

Swap elements:
If the minimum element found is not at the current position of the outer loop, swap the minimum element with the element at the current position. This effectively moves the smallest element to its correct sorted position.

Repeat:
Continue this process until the entire list is sorted
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current element is the minimum
        min_idx = i
        
        for j in range(i + 1, n):
        # Find the actual minimum element in the unsorted part
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(f"Sorted list: {sorted_list}")

