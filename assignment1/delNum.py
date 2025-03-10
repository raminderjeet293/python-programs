def delOdd_NegativeNum(lst):
    return [n for n in lst if n>=0 and n%2==0]
     #used list comprehension to return a list   
listt=eval(input("Enter a list including odd & negative nums:"))
filtered_list=delOdd_NegativeNum(listt)
print("Filtered list:",filtered_list)       