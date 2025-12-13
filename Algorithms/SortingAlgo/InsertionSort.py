"""
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.

1, The insertionSort function takes an array arr as input. It first calculates the length of the array (n).

2, For arrays with more than one element, We start with second element of the array as first element in the array is assumed to be sorted.

3, Compare second element with the first element and check if the second element is smaller then swap them.

4, Move to the third element and compare it with the first two elements and put at its correct position

5, Repeat until the entire array is sorted.
"""




# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current = arr[i]
#         j = i -1
        
#         while j >=0 and arr[j] > current:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = current
        
#     return arr



def insertion_sort(arr):
    for i in range(1, len(arr)):  # we start with the 1st index to its length of array
        
        current = arr[i]  # The first index value is stored in the current
        
        j = i -1  # We store the 1 step back value of i in the j
        
        # There can be multiple element which needs to be checked so we use while loop.
        
        while j >=0 and arr[j] > current:
            
            # j >= 0 ensures that we don't go backward for the start index of array
            
            arr[j+1] = arr[j]
            # shift the larger element one position to the right

            j -= 1
        arr[j+1] = current  
        # insert it at the correct position!

        
    return arr

# Example usage:
my_list = [64, 25, 12, 22, 11]
sorted_list = insertion_sort(my_list)
print(f"Sorted list: {sorted_list}")
        
        
"""

🔍 Mini Example
Sorting [3, 1, 2]
At i = 1:
- current = 1
- Shift 3 to the right → [3, 3, 2]
- Now insert 1 → arr[0] = 1
- Final: [1, 3, 2]
👀 You see that final arr[j + 1] = current is what put 1 in the right place.

This step is the moment of triumph—the point where the key gets inserted into the right place in the lock. Let me know if you’d like a visual walkthrough or a print-based version you can trace line-by-line! 🧠🔐✨


📌 Key Notes:
- Best case (already sorted): O(n)
- Worst case (reverse sorted): O(n²)
- In-place? ✅ (no extra space needed)
- Stable? ✅ (preserves original order of equal elements)


"""