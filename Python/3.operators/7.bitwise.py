'''Bitwise and &
It performs logical AND operation on the integer value after converting an integer to a binary value and gives the result as a decimal value.
It returns True only if both operands are True. Otherwise, it returns False.'''

a = 7
b = 4
c = 5
print(a & b)
print(a & c)
print(b & c)

#Output

4
5
4

'''Bitwise or |
It performs logical OR operation on the integer value after converting integer value to binary value and gives the result a decimal value. 
It returns False only if both operands are True. Otherwise, it returns True.'''

a = 7
b = 4
c = 5
print(a | b)
print(a | c)
print(b | c)

#Output

7
7
5

'''Bitwise xor ^
It performs Logical XOR ^ operation on the binary value of a integer and gives the result as a decimal value.'''

a = 7
b = 4
c = 5
print(a ^ c)
print(b ^ c)

#Output

3
2
1

'''Bitwise 1’s complement ~
It performs 1’s complement operation. 
It invert each bit of binary value and returns the bitwise negation of a value as a result.'''

a = 7
b = 4
c = 3
print(~a, ~b, ~c)
# Output -8 -5 -4

'''Bitwise left-shift <<
The left-shift << operator performs a shifting bit of value by a given number of the place and fills 0’s to new positions.'''

print(4 << 2) 
# Output 16
print(5 << 3)
# Output 40

'''Bitwise right-shift >>
The left-shift >> operator performs shifting a bit of value to the right by a given number of places. Here some bits are lost.'''

print(4 >> 2)
# Output 
print(5 >> 2)
# Output 

