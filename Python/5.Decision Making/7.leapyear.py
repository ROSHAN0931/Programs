
year=int(input("Enter number\n"))

if year%4==0 and year%100!=0:
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("not a leap year")
