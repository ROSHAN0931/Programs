# Function

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def painter():
    print("hello")

painter()

# create a func of add,sub,mul and get input inside the func:-

def add():
    a=int(input())
    b=int(input())
    print("addition is :",a+b)

def sub():
    a=int(input())
    b=int(input())
    print("subtraction is :",a-b)
add()
sub()