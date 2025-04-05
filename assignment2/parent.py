class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printt(self):
        print(f"Parent name: {self.name}, Age: {self.age}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age) 
        super().printt()             

c = Child("Rukmani Devi", 60)
