a=4
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# output: right angle triangle
# * 
# * * 
# * * * 
# * * * * 

a=7
for i in range(1,a+1):
    for j in range(a+1-i):
        print("*",end=" ")
    print()
    
# output
# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 