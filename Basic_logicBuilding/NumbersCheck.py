
# natrual num --> 1 to inifinity
# positive num --> 1 to infinity
# negative num --> -infinity to -1

def sum_of_square_natural_number(n: int) -> int:
    """
    Given a positive integer n, we have to find the sum of squares of first n natural numbers. 
        Examples : 

        Input : n = 2
        Output: 5
        Explanation: 1^2+2^2 = 5

        Input : n = 8
        Output: 204
        Explanation :  1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 = 204 
    """
    
    # Not best approach since n
    
    # return sum([i**2 for i in range(1, n+1)])

    # Best approach
        #1^2 + 2^2 + ......... + n^2 = n(n+1)(2n+1) / 6
    return (n* (n+1)*(2*n +1) ) / 6 
    

def swap_two_number(a, b):

# worst way    
    # num = a
    # num_2 = b
    # b = num
    # a = num_2
    # print(a,b)
    
    # # naive approach
    # temp = a   # temp will store the a value 
    # a = b       # assigning the a value to b  as asked
    # b = temp   # now storing the temp(which is original a value) in b
    # print(a, b)
    
    
    #prefered approach
    # This can be done without creating new var.
    a,b = b,a
    print(a,b)
    print("\n")


if __name__ == "__main__":
    # print(sum_of_square_natural_number(8))
    swap_two_number(3,4)


"""
Find the number closest to n and divisible by m
Last Updated : 13 Feb, 2025

    Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.
    
    Examples: 

    Input: n = 13, m = 4
    Output: 12
    Explanation: 12 is the closest to 13, divisible by 4.

    Input: n = -15, m = 6
    Output: -18
    Explanation: Both -12 and -18 are closest to -15, but-18 has the maximum absolute value.
    # maximum absolute value means greatest value
"""

# num closest to n    and   num divisible by m
# if ouput more than 1 than choose highest

def num_close_to_n_and_DivisibleBy_n(n : int,m : int) ->int:
   
   q:int = int(n/m)
   #To find the closest num we first divide it and take a quotient
   
   # the 1st possible closest number
   n1:int = m *q
   
#    To check the 2nd most closest number, we check th n and m ,multiple greater than 0 if yes than increase the quotient by 1 if not that decrease the queotient by -1
 
   if((n*m )>0 ):
       n2:int = (m * (q+1))
   else: 
       n2:int = (m* (q -1))   # if the m*n is in (-) than we knnow the second most closest has to be lower than n1 so we do (q-1)
    
    
    #Now we need to return the closest value from n
   if (abs(n - n1) < abs(n - n2)) :
        return n1 
        # Now when the value of n1 is less than n2 than the closest value is n1 
    # for example there is 12, and 16 than n1 is the lowest that means n1 is the output so return it.
   return n2   
#else n2 is the closest
   
   

        
print(num_close_to_n_and_DivisibleBy_n(-15,6))