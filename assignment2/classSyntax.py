class student:
    var1=0
    def __init__(self,var):
        self.var=var
        student.var1+=1
    def display(self):
        print("Var=",self.var,student.var1)
st=student(10)
st.display()
st1=student(20)
st1.display()            