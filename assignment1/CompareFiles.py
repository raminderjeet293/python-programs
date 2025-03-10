def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1:
            lines1 = f1.readlines()
        with open(file2, 'r') as f2:
            lines2 = f2.readlines()
        
        if lines1 == lines2:
            print("Both files are identical.")
        else:
            print("The files are different.")
        
        print(f"Total number of lines in {file1}: {len(lines1)}")
        print(f"Total number of lines in {file2}: {len(lines2)}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")
compare_files(file1, file2)