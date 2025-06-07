
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


if __name__ == "__main__":
    # print(sum_of_square_natural_number(8))
    swap_two_number(3,4)

