def countOccurence(lst):
    result=[]
    for n in lst:
        cnt=0
        for j in lst:
            if n==j:
                cnt+=1
        if cnt %2 !=0 and n not in result:
            result.append(n)
    return result        
listt=eval(input("Enter a list:"))
filtered_list=countOccurence(listt)
print("Filtered list containing number with odd no. of occurences:",filtered_list)       