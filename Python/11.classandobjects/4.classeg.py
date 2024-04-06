# Create a class called student,create a variable as name and register using constructor.
# Create a function called display which should display the name and register number of the student.
class student:
    def __init__(self):
        self.name=""
        self.reg=0
    def dis(self):
        print(self.name)
        print(self.reg)
        
ss=student()

ss.name="roshan"
ss.reg=1234

ss.dis()