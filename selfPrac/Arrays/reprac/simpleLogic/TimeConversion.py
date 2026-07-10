# Write a program to read seconds and convert them into hours, minutes and seconds.


def convertSecond(seconds:int):
    
    one_hour = 3600
    one_minute = 60
    
    hours = seconds // one_hour
    # // is integer divison it only provides one value no float or decimal 
    
    
    minute = (seconds % one_hour) // one_minute
    second = seconds % one_minute
    print(hours, minute, second)
    

        
convertSecond(3672)
        