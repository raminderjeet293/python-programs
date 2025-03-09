str = input("Enter a string: ")
stack = []
pairs = {')': '(', '}': '{', ']': '['}

for c in str:
    if c in "({[":
        stack.append(c)
    elif not stack or stack.pop() != pairs[c]:
        print(False)
        break
else:
    print(not stack)