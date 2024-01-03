name = "Roshan"
age = 30
print("Name:", name)
print("Age:", age)

name = "Deekshi"
age = 25
print("Hello, my name is", name, "and I am", age, "years old.")

print("My name is \nRoshan ")

# This line will automatically add a new line before the
# next print statement
print ("I am a technical trainer")
 
# This print() function ends with "**" as set in the end argument.
print ("i love python", end= "->")
print("Welcome to python")



print('My website is ' + 'github.com/RODEEKS')

a,b,=10,1000
print('The value of a is {} and b is {}'.format(a,b))

'''Python “sep” parameter in print()
The print() function can accept any number of positional arguments. To separate these positional arguments, the keyword argument “sep” is used.

Note: As sep, end, flush, and file are keyword arguments their position does not change the result of the code. 

Example

This code is showing that how can we use the sep argument for multiple variables.'''

a=12
b=12
c=2022
print(a,b,c,sep="-")