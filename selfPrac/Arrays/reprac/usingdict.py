fruit_list = ['apple', 'banana', 'apple', 'orange', 'banana']

count = {}

for fruit in fruit_list:
    if fruit not in count:
        count[fruit] = 0
    count[fruit] += 1

print(count)

from collections import defaultdict

new_count = defaultdict(int)

for fruit in fruit_list:
    new_count[fruit] += 1

print(new_count) 