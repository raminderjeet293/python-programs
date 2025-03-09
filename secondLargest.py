listt=eval(input("Enter a list:"))
length=0
for _ in listt:
    length+=1 
for i in range(length):
    for j in range(0,length-i-1):
        if listt[j]>listt[j+1]:
            listt[j],listt[j+1]=listt[j+1],listt[j]
print("Second largest number:", listt[-2])          