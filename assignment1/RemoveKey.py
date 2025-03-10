def removeKey(dict,key):
    if key in dict:
            del dict[k]
    return dict
dictt={"a":1,"b":2,"c":3,"d":4}
print(dictt)
k=input("Enter a key to be deleted from the dictionary:")   
print(removeKey(dictt,k))     