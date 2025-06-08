"""
    The dice problem
    
You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.

Examples:

Input: n = 2
Output: 5
Explanation: For dice facing number 5 opposite face will have the number 2.

Input: 6 = 6
Output: 1
Explanation: For dice facing number 6 opposite face will have the number 1.
"""


# 1st way basic way

def get_dice_number(n):
    match n:
        case 1:
            return 6
        case 2:
            return 5
        case 3:
            return 4
        case 4:
            return 3
        case 5:
            return 2
        case 6:
            return 1
        case _:
            print("Please give number between 1 to 6")     

# Expected approach
#The idea is based on the observation that the sum of two opposite sides of a cubical dice is equal to 7
#So, just subtract the given n from 7 and print the answer

def opposite_side_of_dice(n):
    
    sum = 7 - n    #here whatever number you will add 7 - the provided number will be equal to the opposite no. of that. for e.g if you provide 1 then ans. is 6 likewise if 3 than ans. is 4
    return sum

    # Why 7  answer: 2 + 5 = 7, 1 + 6 = 7, 3+4 =7. The sum of two opposite dice is 7 


if __name__ == "__main__":
    print(get_dice_number(4))
    print("\n")
    print(opposite_side_of_dice(3))