class Grandmother:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mother(Grandmother):
    def __init__(self, name, age, m_name, m_age):
        super().__init__(name, age) 
        self.m_name = m_name
        self.m_age = m_age

class Daughter(Mother):
    def __init__(self, name, age, m_name, m_age, d_name, d_age):
        super().__init__(name, age, m_name, m_age) 
        self.d_name = d_name
        self.d_age = d_age

    def showdetails(self):  
        print(f"Grandmother name: {self.name}, Age: {self.age}")
        print(f"Mother name: {self.m_name}, Age: {self.m_age}")
        print(f"Daughter name: {self.d_name}, Age: {self.d_age}")
        
d = Daughter("Rukmani Devi", 60, "Sita", 45, "Ria", 22)
d.showdetails()