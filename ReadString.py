str = input("Enter the string: ")
with open("output.txt", "a") as file:
    file.write(str + "\n")
print("String appended successfully")

with open("output.txt", "r") as file:
    print("Current contents of the file:")
    print(file.read())