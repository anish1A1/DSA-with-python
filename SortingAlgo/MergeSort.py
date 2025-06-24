"""
Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the divide-and-conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array.

How does Merge Sort work?
Here's a step-by-step explanation of how merge sort works:

Divide:  Divide the list or array recursively into two halves until it can no more be divided.
 
Conquer:  Each subarray is sorted individually using the merge sort algorithm. 

Merge:  The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged. 
"""




def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are leftovers in either list, add them
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list of 0 or 1 elements is already sorted

    # Step 1: Divide the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)




data = [1, 7, 4, 1, 10, 9, 2]
print (merge_sort(data))




"""

Now let's break it down **line by line** and then walk through an **example** to help you deeply understand how it works.

---

## 🔍 What is Merge Sort?

Merge Sort is:

* A **divide and conquer** algorithm.
* Time complexity: **O(n log n)**
* It:

  1. **Divides** the array into halves recursively
  2. **Sorts** each half
  3. **Merges** the sorted halves

---

## ✅ Code Walkthrough with Line-by-Line Explanation

### 🔹 `merge()` Function:

```python
def merge(left, right):
    result = []
    i = j = 0
```

* `left`, `right`: two sorted arrays.
* `i`, `j`: pointers to elements of `left` and `right`.
* `result`: stores the merged sorted array.

---

```python
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
```

* Compares elements at current `i` and `j`.
* Appends the **smaller one** to `result`.
* Moves pointer forward in the array from where the element was taken.

---

```python
    result.extend(left[i:])
    result.extend(right[j:])
```

* If any items are left in `left` or `right`, this adds them.

---

### 🔹 `merge_sort()` Function:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
```

* Base case: a list with 0 or 1 element is **already sorted**, so return it.

---

```python
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
```

* Divides the list into two halves.
* Recursively sorts both halves.

---

```python
    return merge(left_half, right_half)
```

* Merges the two sorted halves using `merge()`.

---

## 🧪 Example: `data = [1, 7, 4, 1, 10, 9, 2]`

Let’s go step-by-step:

---

### 1. Split

```
[1, 7, 4, 1, 10, 9, 2]
⬇
[1, 7, 4]         [1, 10, 9, 2]
⬇                ⬇
[1] [7, 4]        [1, 10] [9, 2]
     ⬇                ⬇
   [7] [4]         [1] [10]     [9] [2]
```

---

### 2. Merge

Start merging sorted pieces:

```
merge([7], [4]) → [4, 7]
merge([1], [4, 7]) → [1, 4, 7]

merge([1], [10]) → [1, 10]
merge([9], [2]) → [2, 9]
merge([1, 10], [2, 9]) → [1, 2, 9, 10]

merge([1, 4, 7], [1, 2, 9, 10]) → [1, 1, 2, 4, 7, 9, 10]
```

---

### ✅ Final Output:

```python
[1, 1, 2, 4, 7, 9, 10]
```

---

## 🧠 Summary:

| Step    | Description                                 |
| ------- | ------------------------------------------- |
| Divide  | Recursively split the array into two halves |
| Conquer | Sort each half recursively                  |
| Combine | Merge the two sorted halves                 |

---

## ✅ Output:

```python
data = [1, 7, 4, 1, 10, 9, 2]
print(merge_sort(data))
# ➜ Output: [1, 1, 2, 4, 7, 9, 10]
```

---

Would you like a visual tree diagram showing how merge sort splits and merges?


"