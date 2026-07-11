#Write a program to display all natural numbers from 1 to n in reverse order.

def reverseOrder(nums):
    new_nums = []
    for i in range(len(nums), 0, -1):
        print(i)
        new_nums.append(i)
        
    print("New reversed order is ",new_nums)

reverseOrder([1,2,3,4,5,6])

