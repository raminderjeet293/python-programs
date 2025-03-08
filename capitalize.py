def cap(str):
    result=""
    for i in range(len(str)):
        if i%2==0:
            result+=str[i].lower()
        else:
              result+=str[i].upper() 
    return result  
str=input("Enter a string:")
print(cap(str))          
   
