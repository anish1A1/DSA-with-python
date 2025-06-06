fruits : list[int] = [1, 2, 3, 4, 5]   # list with data structure of integers
print([x for x in fruits if x % 2 ==0])    #list comprehension

def checkIntEven(x :int) -> int:
    return x % 2 == 0

print(list(filter(checkIntEven, fruits)))

"""
    Second Largest Element in an Array
    Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

    Note: If the second largest element does not exist, return -1.

    Examples:

    Input: arr[] = [12, 35, 1, 10, 34, 1]
    Output: 34
    Explanation: The largest element of the array is 35 and the second largest element is 34.

    Input: arr[] = [10, 5, 10]
    Output: 5
    Explanation: The largest element of the array is 10 and the second largest element is 5.

    Input: arr[] = [10, 10, 10]
    Output: -1
    Explanation: The largest element of the array is 10 there is no second largest element.
"""

def get_second_largest(arr: list[int]) -> int:
    n = len(arr)
    
    second_largest = -1
    largest = -1
    
    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest
        

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(get_second_largest(arr))