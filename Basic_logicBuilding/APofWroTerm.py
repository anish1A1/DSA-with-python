"""
Nth term of AP from First Two Terms

Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series. 
Examples :

Input : a1 = 2,  a2 = 3,  n = 4
Output : 5
Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

Input : a1 = 1, a2 = 3, n = 10
Output : 19
Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.
"""


# Basic approach
def get_nth_term(a1, a2, n:int):
    nthTerm = a1   #Since the first term is a1 the given value
    end:int = a2-a1             #This formula to find the steps of increment
    for i in range(1,n):   #We started from index 1 sice we need to find the nth from starting and 0th term is a1
        nthTerm +=end
    return nthTerm

# Time Complexity - O(n)
# Auxiliary Space - O(1)   



# Expected Approach

"""
[Expected Approach] - Using the Formula for nth Term
To find the nth term in the Arithmetic Progression series we use the simple formula . 

We know the Arithmetic Progression series is like =  2, 3, 4, 5, 6. …. … 
In this series 2 is the first term and 3 is the second term of the series . 
Common difference = a2 - a1 =  3 – 2 = 1 (Difference common in the series). 
so we can write the series as :
t1 = a1 
t2 = a1 + (2-1) * d 
t3 = a1 + (3-1) * d 
. 
. 
. 
tN = a1 + (n-1) * d 

tN = a1 + (n-1) * (a2-a1) 
"""

def nthTermOfAP(a1,a2,n):
    #Using fromula
    #tn = a + (n-1) *d ,where d = a2-a1
    nthTerm = a1 + (n-1) * (a2-a1)
    return nthTerm


print(get_nth_term(a1=2, a2=5,n=3) )   
print(nthTermOfAP(a1=2, a2=5,n=3) )   
