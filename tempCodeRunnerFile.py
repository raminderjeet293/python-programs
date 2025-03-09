def checkSubstring(str,sub):
    if sub in str:
        return "Substring is in given string"
    else:
        return "Substring not in given string"   
        
str=input("Enter String: ")
sub= input("Enter Sub-String: ")       
print(checkSubstring(str,sub))