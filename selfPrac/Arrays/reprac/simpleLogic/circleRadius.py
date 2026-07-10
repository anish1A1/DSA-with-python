# Write a program to read the radius of a circle and print its area and circumference.

import math

def circle(radius):
    
    print("Radius Is",radius)
    
    area = math.pi * radius ** 2
    
    circumference = 2 *math.pi * radius
    
    print(f"Area is {area:.2f} and Circumference is {circumference}")
    
    return area, circumference

circle(5) 