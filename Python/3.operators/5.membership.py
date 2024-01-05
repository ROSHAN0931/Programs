'''Python’s membership operators are used to check for membership of objects in sequence, such as string, list, tuple. 
It checks whether the given value or variable is present in a given sequence. If present, it will return True else False.

In Python, there are two membership operator in and not in'''

'''In operator
It returns a result as True if it finds a given object in the sequence. Otherwise, it returns False.

Let’s check if the number 15 present in a given list using the in operator.'''

my_list = [11, 15, 21, 29, 50, 70]
number = 15
if number in my_list:
    print("number is present")
else:
    print("number is not present")

Output

number is present

'''Not in operator
It returns True if the object is not present in a given sequence. Otherwise, it returns False'''

my_tuple = (11, 15, 21, 29, 50, 70)
number = 35
if number not in my_tuple:
    print("number is not present")
else:
    print("number is present")

Output

number not is present

