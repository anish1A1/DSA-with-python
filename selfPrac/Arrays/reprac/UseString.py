txt = "The best things in life are free!".upper()
generate = [i.upper().replace('!', '😏') for i in txt]
print(generate)
print(txt)

print('free'.upper() in txt)

print('expensive' not in txt)

print(txt[::-1])

print(txt.strip())
removing_char = "THe"
print(txt.strip(removing_char)) 