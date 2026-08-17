

def merge(arr):
    if len(arr) <=1:
        return arr 
    
    mid = len(arr) // 2
    
    left_half = merge(arr[:mid])
    right_half = merge(arr[mid:])
    
    return arr_merge(left_half, right_half)

def arr_merge(left_half, right_half):
    result = []
    i=j=0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i+=1
        else:
            result.append(right_half[j])
            j+=1
    
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result

print(merge([54,26,93,17,77,31,44,55]))

# Now seeing how the code works



def merge(arr):
    if len(arr) <=1:
        return arr 
    
    mid = len(arr) // 2
    
    left_half = merge(arr[:mid])
    print("Left Half in recursion: ",left_half)

    right_half = merge(arr[mid:])
    print("Right Half in recursion: ",right_half)
    
    return arr_merge(left_half, right_half)

def arr_merge(left_half, right_half):
    result = []
    i=j=0
    print("The current result is: ", result)
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            print("Inside the conditional stmt: ", left_half[i], right_half[j])
            result.append(left_half[i])
            i+=1
        else:
            result.append(right_half[j])
            j+=1
        print("The after result is: ", result)
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result

print(merge([54,26,93,17,77,2,31,44,55]))


"""
Great question — the difference between `append()` and `extend()` is exactly what makes merge sort work correctly here.

---

### 🔎 `append()`
- Adds the **entire object** as a single element to the list.
- Example:
  result = [1, 2]
  result.append([3, 4])
  print(result)  # [1, 2, [3, 4]]
- Notice how `[3,4]` became **one nested list** inside `result`.

---

### 🔎 `extend()`
- Takes an **iterable** (like a list or slice) and adds each element individually to the list.
- Example:
  result = [1, 2]
  result.extend([3, 4])
  print(result)  # [1, 2, 3, 4]

- Here `[3,4]` was “unpacked” and its elements were added one by one.

---

### 🔎 In Your Merge Sort
At the end of merging:

result.extend(left_half[i:])
result.extend(right_half[j:])

- `left_half[i:]` is the **remaining elements** from the left side.  
- `right_half[j:]` is the **remaining elements** from the right side.  
- Using `extend()` ensures those leftover elements are added directly into `result` as numbers, not as nested lists.

If you mistakenly used `append()`:

result.append(left_half[i:])
you’d end up with something like:

[17, 26, 31, [44, 54], [55, 77, 93]]

which breaks comparisons later because you’re mixing integers and lists.

---

### ✅ Key Catch
- `append()` → adds one item (could be a list, causing nesting).  
- `extend()` → flattens and adds each element individually.  
- That’s why merge sort must use `extend()` to keep the result list flat and sorted.

---

Would you like me to show you a **mini demo with prints** comparing `append()` vs `extend()` on the same slices, so you can *see* the difference in output side by side?
"""