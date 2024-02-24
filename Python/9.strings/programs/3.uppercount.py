# Write a program that takes a string as input and counts the number of 
# uppercase letters in the string.


a=input("Enter string : ")
u=0
l=0
for i in a:
    if i.isupper():
        u=u+1
    if i.islower():
        l=l+1
print("total upper is ",u)
print("total lower is ",l)