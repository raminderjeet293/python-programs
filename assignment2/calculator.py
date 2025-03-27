class cal:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print("Addition:",self.n1+self.n2)
    def sub(self):
        print("subtraction:",self.n1-self.n2)
    def mul(self):
        print("Multiplication:",self.n1*self.n2)
    def div(self):
        if self.n2!=0:
              print("Division:",self.n1/self.n2)       
        else:
            print("Division not allowed by zero")          
c=cal(30,40)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())           
