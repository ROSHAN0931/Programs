for i in range(1,11):
    for j in range(1,11):
        print(i * j ,end='  ')
    print()

# rectangle    

for i in range(1,5):
    for j in range(1,7):
        print("*",end=" ")
    print()

#square

for i in range(10):
    for j in range(10):
        print("#",end=' ')
    print()
    
#right-angle triangle

row=int(input("enter row: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
    
#continue 
a=[2,4,6]
b=[2,4,6]

for i in a:
    for j in b:
        if i==j:
            continue    
        print(i,"x",j,"=",i*j)

# output
# 2 x 4 = 8
# 2 x 6 = 12
# 4 x 2 = 8
# 4 x 6 = 24
# 6 x 2 = 12
# 6 x 4 = 24