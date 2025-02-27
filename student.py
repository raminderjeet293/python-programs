#11. WAPto store students information like admission number, roll number, name and marks in a dictionary and display information on the basis of admission number.
def stud():
    dict={}
    n=int(input("Enter number of Students:"))
    for i in range(n):
        print(f'Enter details of Student {i+1}')
        roll_no=int(input("Enter Roll No.:"))
        name=input("Enter Name:")
        marks=int(input("Enter Marks:"))
        admission_no = int(input("Enter Admission No.:"))
        dict[admission_no]={
            'Roll no': roll_no,
            'Name': name,
            'Marks': marks,
        }
    print("Student Details are:")
    for admn,info in dict.items():
        print("Admission Num:",admn)
        print('Roll num:',info['Roll no'])
        print("Name:",info['Name'])
        print("Marks:",info['Marks'])
stud()