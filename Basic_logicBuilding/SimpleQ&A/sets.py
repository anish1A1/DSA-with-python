set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1 | set2
print(union_set)

insertion_set = set1 & set2 
print(insertion_set)

difference_set = set1 - set2
print(difference_set)

symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)

set1.discard(2)
print(set1)