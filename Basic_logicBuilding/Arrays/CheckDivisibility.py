"""
3622. Check Divisibility by Digit Sum and Product
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

The digit sum of n (the sum of its digits).

The digit product of n (the product of its digits).

Return true if n is divisible by this sum; otherwise, return false.

 

Example 1:

Input: n = 99

Output: true

Explanation:

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

Example 2:

Input: n = 23

Output: false

Explanation:

Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

 

Constraints:

1 <= n <= 10^6

"""


def checkDivisibility( n: int) -> bool:
    value = f"{n}"
    sum = 0
    product = 1
    
    if len(value) == 1:
        return True
    
    for i in value:
        i = int(i)
        sum += i
        product *= i
        
    print(sum, product)
    total = sum + product
    
    if n % total == 0:
        return True 
    return False
        
        
        
print(checkDivisibility(n=99))
print(checkDivisibility(n=23))
print(checkDivisibility(n=10))

