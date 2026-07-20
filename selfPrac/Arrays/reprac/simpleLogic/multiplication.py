#29. Write a program to display the multiplication table of a number n.


def multiplication(num, multiplication_table_num):
    
    for i in range(1,multiplication_table_num + 1):
        print(f"{num} X {i} =", num*i)
    
print(multiplication(7, 12))
        