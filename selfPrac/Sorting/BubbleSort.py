


def BubbleSorting(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n-1):
            if nums[j + 1] > nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            print("Array being Sorted: ",nums, "with index", i )
    return "Array after Bubble Sort:",nums
   
nums =[9,16,6,26,0]     
print(BubbleSorting(nums))
print("\n")

def BubbleSortingReverse(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
        for j in range(n-1):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            print("Array being Sorted: ",nums, "with index", i )
    return "Array after Reverse Bubble Sort:",nums

nums =[9,16,6,26,0]     
print(BubbleSortingReverse(nums))


def UserInputBubbleSort():
    arr = []
    num = int(input("Enter how many numbers:"))
    
    print('Enter values')
    for _ in range(num):
        arr.append(int(input()))
    n = len(arr) 
    for _ in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                
    return "The Sorted values of user input is: ",arr

print(UserInputBubbleSort())