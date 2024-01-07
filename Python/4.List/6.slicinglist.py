
#sliced_list = List_Name[startIndex:endIndex]

a=["red","blue","green","black","yellow"]
print(a[0:2]) #cut first element from the list
print(a[2:]) #cut last element from the list
print(a[1:2]) #cut 2 element from the list

print(a[1:-1]) #cut 2 and 3 element from list
a.remove("green")
print(a)
print(a[1:-1])
