def count(s):
    words = s.lower().split()
    w_f = {}
    for word in words:
        if word in w_f:
            w_f[word] += 1
        else:
            w_f[word] = 1
    return w_f

s = input("Enter the string: ")
w_f = count(s)
print(w_f)