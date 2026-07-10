# Write a program to read the marks of 5 subjects and print the total and average.


def marks(subjects):
    # Assuming a subject total mark is 100

    total = sum(subjects)
    average = total / len(subjects)
    print(total, average)
    
marks([56,78,91,64,67])
# Time complexity is 0(n) sinec sum is an iterable
     