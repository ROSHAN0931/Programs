
a=int(input("Enter number\n"))
b=int(input("Enter number\n"))
c=int(input("Enter number\n"))

if a==b and b==c:
    print("3 numbers are equal")
elif a!=b and b!=c and c!=a:
    print("All are different")
else:
    print("2 numbers are same")
