def bubbleSort(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1-j):
                if lst[i]>lst[i+1]:
                     lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst
listt=eval(input("Enter list elements:"))
print("Original list:",listt)
print("Bubble sorted list:",bubbleSort(listt))                 