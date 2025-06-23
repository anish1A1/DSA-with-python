"""
QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

How does QuickSort Algorithm work?
QuickSort works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

There are mainly three steps in the algorithm:

Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).

Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.

Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).

Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
"""


def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        partion_index = partition(array, low, high)
        quickSort(array, low, partion_index - 1)
        quickSort(array, partion_index + 1, high)


data = [1, 7, 4, 1, 10, 9, 2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

# If we call this in a function then in the quick_sort function in the end write this line --> return arr


print('Sorted Array in Ascending Order:')
print(data)



"""

data = [1, 7, 4, 1, 10, 9, 2]


We're using the version where the **rightmost element is the pivot**, i.e., `pivot = array[high]`.

---

### 🧩 Step-by-Step Dry Run

We’ll trace the recursive calls, pivot selections, swaps, and the final sort.

---

#### 🔹 First Call: `quickSort([1, 7, 4, 1, 10, 9, 2], 0, 6)`
- **Pivot** = `2`
- Start: `i = -1`

Loop through j = 0 → 5:
- `1 <= 2` → i = 0 → swap `1` with `1`
- `7 > 2` → skip
- `4 > 2` → skip
- `1 <= 2` → i = 1 → swap `7` with `1` → `[1, 1, 4, 7, 10, 9, 2]`
- `10 > 2` → skip
- `9 > 2` → skip

End: swap `pivot (2)` with `array[i+1] = array[2]`  
→ Final state: `[1, 1, 2, 7, 10, 9, 4]`  
→ Pivot placed at **index 2**

---

#### 🔹 Recurse Left: `quickSort([1, 1, 2, 7, 10, 9, 4], 0, 1)`
- Pivot = `1`
- `i = -1`

Loop j = 0:
- `1 <= 1` → i = 0 → swap `1` with `1`

End: swap pivot `1` with `array[1]`  
→ No actual change  
→ Pivot placed at index 1

Now recurse left: `quickSort(..., 0, 0)` → base case  
Recurse right: `quickSort(..., 2, 1)` → base case

✔️ Left side done: `[1, 1]`

---

#### 🔹 Recurse Right: `quickSort([1, 1, 2, 7, 10, 9, 4], 3, 6)`
- Pivot = `4`
- `i = 2`

j = 3 to 5:
- `7 > 4` → skip
- `10 > 4` → skip
- `9 > 4` → skip

Swap pivot `4` with `array[i+1] = array[3]`  
→ Swap `7` and `4` → `[1, 1, 2, 4, 10, 9, 7]`  
→ Pivot placed at index 3

---

#### 🔹 Recurse Right: `quickSort([1, 1, 2, 4, 10, 9, 7], 4, 6)`
- Pivot = `7`
- `i = 3`

j = 4 to 5:
- `10 > 7` → skip
- `9 > 7` → skip

Swap `7` with `array[4]` → `[1, 1, 2, 4, 7, 9, 10]`  
→ Pivot placed at index 4

---

#### 🔹 Final Recursions
- `quickSort(..., 4, 3)` → done
- `quickSort(..., 5, 6)`  
  - Pivot = `10`, `i = 4`
  - `9 < 10` → i = 5, swap `9` with `9`
  - Swap `10` with `10`  
  - Pivot at index 6 → done

---

### ✅ Final Sorted Array:

```python
[1, 1, 2, 4, 7, 9, 10]
```




"""