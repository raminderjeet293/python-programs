str=input("Enter a String:").lower()
reverse=""
for char in str:
    reverse = char + reverse
if str == reverse:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")          