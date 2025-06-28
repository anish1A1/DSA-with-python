my_list = [0, 10, 12, 13, 14, 15, 16, 17, 18, 19]

slice1 = my_list[::]   #This will copy the my_list in slice1

slice1[2] = 3   #here only the copied array will change not the my_list array

print(slice1)
print(my_list)

slice2 = my_list[1:5:2]
print(slice2)


slice3 = my_list[1:]   #This will add all element from index 1 (inclusive)

slice4 = my_list[:6] #This will add all element before index 6 (exclusive)

print(f"Slice3 after index 1(inclusive) {slice3}")

print(f"Slice4 uptil index 6(exclusive) {slice4}")

slice5 = my_list[::-1]  #This will copy the my_list from index -1 (last)
print(f"Copying list in reverse {slice5}")



slice6 = my_list[:]
slice6.append("New")  # we can also add char. in here and this will not change the main array
print(slice6)
print(my_list)


slice7 = my_list[:-3]  #Here index -3 will be exclusive and all the element before that will be copied in slice7
print(slice7)