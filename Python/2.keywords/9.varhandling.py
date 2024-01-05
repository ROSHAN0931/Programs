#Variable Handling Keywords: del, global, nonlocal

'''The del keyword is used to delete the object.
The global keyword is used to declare the global variable. 
A global variable is a variable that is defined outside of the method (block of code). 
That is accessible anywhere in the code file.
Nonlocal variables are used in nested functions whose local scope is not defined. 
This means that the variable can be neither in the local nor the global scope.'''

price = 900  # Global variable

def test1():  # defining 1st function
    print("price in 1st function :", price)  # 900

def test2():  # defining 2nd function
    print("price in 2nd function :", price)  # 900

# call functions
test1()
test2()

# delete variable
del price
