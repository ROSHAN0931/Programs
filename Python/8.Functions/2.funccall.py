# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Get input from user and pass it to a function and display even or odd:-

def evenodd(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
a=int(input())
evenodd(a)

# Get 2 input from user pass to fun and print the numbers from range

def printrange(a,b):
    for i in range(a,b):
        print(i)

a=int(input())
b=int(input())
printrange(a,b)


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# Number of Arguments:
# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args:
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments:
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Default Parameter Value:
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")