def nestedSum(l):
    total=0
    for item in l:
        if isinstance(item,list):
            total+=nestedSum(item)
        else:
            total+=item
    return total

listt=[1,[2,3,[3]],90,[2,8]]  
#listt=eval(input("Enter list:"))   
totalSum=nestedSum(listt)
print(f'Sum of items in nested List are:{totalSum}')       