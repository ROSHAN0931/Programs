'''+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
// Floor division)
℅ (Modulus)
** (Exponentiation)'''

x = 10
y = 40
print(x + y)
# Output 50

name = "Kelly"
surname = "Ault"
print(surname + " " + name)
# Output Ault Kelly

x = 10
y = 40
print(y - x)
# Output 30

x = 2
y = 4
z = 5
print(x * y)
# Output 8 (2*4)
print(x * y * z)
# Output 40 (2*4*5)

name = "Jessa"
print(name * 3)
# Output JessaJessaJessa

'''Note:
The division operator performs floating-point arithmetic. Hence it always returns a float value.
Don’t divide any number by zero. You will get a Zero Division Error: Division by zero'''

x = 2
y = 4
z = 8
print(y / x)
# Output 2.0
print(z / y / x)
# Output 1.0
# print(z / 0)  # error

'''Floor division //
Floor division returns the quotient (the result of division) in which the digits after the decimal point are removed. In simple terms, It is used to divide one value by a second value and gives a quotient as a round figure value to the next smallest whole value.

It works the same as a division operator, except it returns a possible integer. The // symbol denotes a floor division operator.

Note:

Floor division can perform both floating-point and integer arithmetic.
If both operands are int type, then the result types. If at least one operand type, then the result is a float type.'''

x = 2
y = 4
z = 2.2

# normal division
print(y / x)
# Output 2.0

# floor division to get result as integer
print(y // x)
# Output 2

# normal division
print(y / z)  # 1.81

# floor division.
# Result as float because one argument is float
print(y // z)  # 1.0

x = 15
y = 4

print(x % y)
# Output 3

num = 2
# 2*2
print(num ** 2) 
# Output 4

# 2*2*2
print(num ** 3)
# Output 8
