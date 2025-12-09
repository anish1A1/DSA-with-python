my_list = [0, 10, 12, 13, 14, 15, 16, 17, 18, 19]


copyList = my_list[::] #copy

my_list.append([2,3])

print(my_list)
print(copyList)

revCopy = my_list[::-1]
print(revCopy)

slice7 = my_list[:-3]
print(slice7)