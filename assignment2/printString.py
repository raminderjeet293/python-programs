class MyString: 
    def get_String(self):
        self.s = input("enter str:")
    def print_String(self):
        print("String:", self.s)

obj = MyString() 
obj.get_String()
obj.print_String()  