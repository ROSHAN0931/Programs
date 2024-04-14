def add(a):
    print(a)
add(10)

def add(a=20):
    print(a)
add()

def add(a,b=3):
    print(a+b)
add(1)

def add(a,b,c=11):
    print(a+b+c)
add(1,2)
add(1,2,3)

# so i can use this add func for adding 2 numbers and also for 3 numbers