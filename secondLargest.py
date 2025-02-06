listt=[111,33,100,55,88,99]
#length
length=0
for _ in listt:
    length+=1
print(length)   
#sorting 
for i in range(length):
    for j in range(0,length-i-1):
        if listt[j]>listt[j+1]:
            listt[j],listt[j+1]=listt[j+1],listt[j]
print(listt)  
print("Second largest number:", listt[-2])          