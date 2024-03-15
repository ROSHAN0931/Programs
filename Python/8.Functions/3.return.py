# return keyword

def painter():
    return "i am a painter"

p=painter()
print(p)

def value():
    return 10

a=value()
print(a)

# Return Values
# To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.)
#and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# put in the pass statement to avoid getting an error.

