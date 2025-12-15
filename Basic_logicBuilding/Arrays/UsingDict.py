counts = {}
fruit_list = ['apple', 'banana', 'apple', 'orange', 'banana']

for fruit in fruit_list:
    if fruit not in counts:
        counts[fruit] = 0
    counts[fruit] += 1
    
print(counts)

from collections import defaultdict

new_counts = defaultdict(int)

for fruit in fruit_list:
    new_counts[fruit] += 1
    
print(new_counts)