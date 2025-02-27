def findIndex(l,k):
    for i in range(len(l)):
        if k==l[i]:
            print(i)
    print(f'Index of {k} is {i}')        
listt=eval(input("Enter a list:"))
key=int(input("Enter Key to be searched:"))
findIndex(listt,key)
