
"""
Calculate the sum of Natural numbers
for e.g:
for n = 5, sum = 1 +2 +3 + 4 + 5  = 30
"""

def sum(n):
    if (n == 1):
        return 1
    
    return n + sum(n-1)

print(sum(5))