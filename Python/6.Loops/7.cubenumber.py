# Read 5 numbers and find the cube:- 

a=[]
b=int(input("Enter number"))
for i in range(b):
    num=int(input("enter num "+str(i+1)+" : "))
    a.append(num)
    print("Cube of "+str(i+1)+" is : "+str(num*num*num))