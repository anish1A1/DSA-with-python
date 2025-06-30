
# To find the largest element in an array.


def findLargest(arr):
    arr.sort()
    return arr[-1]

# 0(nlog) and space 0(1)  since sorting takes 0(nlogn)



def findLargestOptimal(arr):
    largest = arr[0]   #ASsusme first index is largest
    
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest
# 0(n)   and space 0(1)

nums = [2,43,65,231,5]
print(findLargest(nums))
print(findLargestOptimal(nums))
