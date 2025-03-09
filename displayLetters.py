def displayLetters(str1,str2):
    result=""
    for ch in str1:
       if ch not in str2:
          result+=ch
    return result      
str1=input("Enter String1:")
str2=input("Enter String2:")
print(displayLetters(str1,str2))
            