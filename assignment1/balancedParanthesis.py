def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack
s = input("Enter a string: ")
if is_balanced(s):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")