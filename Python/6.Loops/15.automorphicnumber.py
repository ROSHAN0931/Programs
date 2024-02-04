a=int(input("enter number: "))
sq=a*a
t=0

while a>0:
    if a%10 != sq%10:
        t=1
        print("not automorphic")
        break
    sq=sq//10
    a=a//10

if t==0:
    print("automorphic number")
    
# 5=15, 25=125    