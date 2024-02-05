a=input("enter input: ")

d=l=0

for i in a:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        continue

print("Digit: ",d)
print("Letter: ",l)
