#Set name and pass,then get input for name and pass,
# now if both name and pass same means print true or false:-

def check(a,b):
    if name==a and b==pas:
        return True
    else:
        return False

name="roshan"
pas="123"

n=input("enter name: ")
p=input("enter pass: ")

print(check(n,p))

# Get 2 input ,pass to fn and return the sum of 2 numbers and mul with one more number:-

def add(a,b):
    return a+b

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

print("addition of a and b is : ",add(a,b))
d=add(a,b)*c
print("multiplication : ",d)