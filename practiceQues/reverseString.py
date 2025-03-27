#1.	Write a program to reverse a String using Slicing
def reverseString(str):
    newStr=str[::-1]
    return newStr
n=input("Enter a string to reverse:")
print("Reversed String:",reverseString(n))
