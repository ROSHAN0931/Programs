'''Identity operators
Use the Identity operator to check whether the value of two variables is the same or not. 
This operator is known as a reference-quality operator because the identity operator compares values according to two variables’ memory addresses.

Python has 2 identity operators is and is not.

is operator
The is operator returns Boolean True or False. It Return True if the memory address first value is equal to the second value. Otherwise, it returns False.'''

x = 10
y = 11 
z = 10
print(x is y) # it compare memory address of x and y 
print(x is z) # it compare memory address of x and z

Output

False
True

'''is not operator
The is not the operator returns boolean values either True or False. 
It Return True if the first value is not equal to the second value. Otherwise, it returns False.'''

x = 10
y = 11 
z = 10
print(x is not y) # it campare memory address of x and y 
print(x is not z) # it campare memory address of x and z

Output

True
False

