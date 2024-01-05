#and
print(True and False)  # False
# both are True
print(True and True)  # True
print(False and False)  # False
print(False and True)  # false

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")

Output

False
True
False
False
 8

'''In the case of arithmetic values, Logical and always returns the second value; as a result, see the following example.'''

print(10 and 20) # 20
print(10 and 5)  # 5
print(100 and 300) # 300

#or

print(True or False)  # True
print(True or True)  # True
print(False or False)  # false 
print(False or True)  # True

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 or b < 0:
    # at least one expression is true so conditions is true
    print(a + b)  # 6
else:
    print("Do nothing")

Output
True
True
False
True
6

'''In the case of arithmetic values, Logical or it always returns the first value; as a result, see the following code.'''

print(10 or 20) # 10
print(10 or 5) # 10
print(100 or 300) # 100

#not

print(not False)  # True return complements result
print(not True)  # True return complements result

# actual use in code
a = True

# Logical not
if not a:
    # a is True so expression is False
    print(a) 
else:
    print("Do nothing")

Output

Do nothing

'''In the case of arithmetic values, Logical not always return False for nonzero value.'''

print(not 10) # False. Non-zero value
print(not 1)  # True. Non-zero value
print(not 5)  # False. Non-zero value
print(not 0)  # True. zero value



