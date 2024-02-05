a=int(input("enter the number: "))

for i in range(1,a+1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
# 16
# 17
# fizz
# 19
# buzz
