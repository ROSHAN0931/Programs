# Create a class called student,create a variable as name and register using constructor.
# Create a function called display which should display the name and register number of the student.
# class student:
#     def __init__(self):
#         self.name=""
#         self.reg=0
#     def dis(self):
#         print(self.name)
#         print(self.reg)
        
# s1=student()
# s2=student()

# s1.name="roshan"
# s1.reg=1234
# s2.name="deekshi"
# s2.reg=56789

# s1.dis()
# s2.dis()

# Create a class called fruit , create a variable called color using __init__ method ,create an object called apple 
# "Pass the color variable as a parameter through object."

# class fruit:
#     def __init__(self,c): 
#         # it will show error ,if u hv only self!!
#         self.color=c

# apple=fruit("red")
# print(apple.color)

# Create a class teacher, create a variable = name and reg number using constructor ,create a fun called display 
# which shd display the name and reg number of the teacher
# Create 2 obj t1,t2 and pass the name reg num value through obj.
# class teacher:
#     def __init__(self,n,r):
#         self.name=n
#         self.reg=r
#     def dis(self):
#         print("Name is : ",self.name)
#         print("Reg is : ",self.reg)
    
# t1=teacher("Roshan",9)
# t2=teacher("Deekshi",31)

# t1.dis()
# t2.dis()

# Create a class calculator,create 2 variables a and b , create a func called add,sub,mul,div all func shd take 2 var
# as parameter . Pass a and b value through object.

class calculator:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def add(self):
        print("Addition is : ",self.a + self.b)
    def sub(self):
        print("Subtraction is : ",self.a - self.b)
    def mul(self):
        print("Multiplication is : ",self.a * self.b)
    def div(self):
        print("Division is : ",self.a / self.b)
    
v=calculator(10,5)
v.add()
v.sub()
v.mul()
v.div()