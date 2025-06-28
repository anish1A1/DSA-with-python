

txt = "The best things in life are free!".upper()
genrate = [i.upper().replace('!', '') for i in txt]
print(genrate)

print(txt)
print('free'.upper() in txt)

print('expensive' not in txt)


print(txt[::-1])

revoming_char = "The"
print(txt.strip())  #strips sremoves the whitespace from the beginning or the end a

print(txt.strip(revoming_char)) #Now strip will remove the chars given inside 

a = "Hello, World"
print(a.replace('Hello', "Not Today"))
print(a.replace('H', "F"))

print(a.split(","))  #This will split the word according the chars given in it.
print(a.split("lo"))  #Return an array of string.



a = "Normal"
b = "Human"

print(a + b)  #concatenating strings 
print(a + " " + b)


price = 29
print(f"The price is ${price:.2f} dollars")


txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)

j1 = ''
j2 = ['bc']

j3 = j1.join(j2)  #This will join two arrays in middle of j1 if it has values (if added array its value should be string).
print(j3)

print(''.join(['1','2',"3"]))  #Array is joined but the array should be string.


"""
Python strings are a fundamental data type for practicing Data Structures and Algorithms (DSA) due to their versatility in representing and manipulating textual data. They are immutable sequences of characters, meaning once created, their content cannot be directly modified, and any "modification" operation actually creates a new string.

Key Concepts and Operations for DSA Practice:
Immutability:
Understanding that string operations like concatenation or replacement create new string objects is crucial for efficiency considerations.

Slicing:
Extracting substrings using [start:end:step] is essential for many string-based problems.

String Methods:
Python offers a rich set of built-in string methods for common tasks:
len(): Determines string length.
upper(), lower(), capitalize(), title(), swapcase(): For case manipulation.
strip(), lstrip(), rstrip(): For removing whitespace.
replace(): For replacing substrings.
split(), join(): For splitting strings into lists and joining lists into strings.
find(), index(), count(): For searching and counting characters/substrings.
startswith(), endswith(): For checking prefixes and suffixes.

Concatenation and Repetition:
Using + for concatenation and * for repetition are basic but important operations. For efficient concatenation of many strings, "".join(list_of_strings) is preferred.

Iterating through Strings:
Strings can be iterated character by character using for loops.

Common DSA Problems Involving Strings:
Palindrome Check: Determining if a string reads the same forwards and backward.
Anagram Check: Verifying if two strings are anagrams of each other (contain the same characters with the same frequencies).
Longest Substring Without Repeating Characters: Finding the longest substring within a given string that does not contain any repeated characters.
String Reversal: Reversing a string or reversing words within a string.
Pattern Matching: Searching for occurrences of a specific pattern within a larger string (e.g., using algorithms like KMP).
Character Frequency Counting: Determining the frequency of each character in a string.
String Compression: Compressing a string by replacing repeated characters with a count.
Practicing these problems helps solidify understanding of string manipulation, algorithmic thinking, and efficient data handling in Python.
"""