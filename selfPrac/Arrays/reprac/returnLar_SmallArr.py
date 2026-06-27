# to return largest and smallest numbers in each array. total 2 numbers

def small_large_numb_1(arrays) -> list:
    
    sorted_arr =  sorted(arrays)
    sml, lar = sorted_arr[0], sorted_arr[-1]
    return [sml, lar]
print(small_large_numb_1([1,34,6,8,9,0]))

# time = 0(nlognn) , space = 0(n)

def small_large_numb_2(arr) -> list:    
    sml = float('inf')
    lar = float('-inf')
    
    for num in arr:
        if num < sml:
            sml = num
        elif num > lar:
            lar = num
    return [sml, lar]
             
print(small_large_numb_2([1,34,6,8,9,0]))

# time 0(n), space 0(1)