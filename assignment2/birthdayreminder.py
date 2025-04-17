from datetime import datetime

with open("birthdays.txt", "a") as f:
    f.write("Raminder,06-04-2000\n") 

today = datetime.now().strftime("%d-%m")
with open("birthdays.txt", "r") as f:
    for line in f:
        name, date = line.strip().split(",")
        if date.startswith(today):
            print(f"Today is {name}'s birthday!")
