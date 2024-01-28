# List
# 1.allows duplicate
# 2.any type of data can be sorted
# 3.we can modify,add,remove,insert,append,extend,pop 

a=[1,2,3,4]
print(type(a))
print(a)
a.append(True)
a.append("roshan")
a.append(9.31)
a.append(1)
print("after appending: ",a)
a.insert(0,11)
print("after inserting: ",a)
a[3]="deekshi"
print("after modifying: ",a)
a.pop(2)
print("after removing: ",a)
a.pop()
print("automatically remove last item: ",a)
b=["r",'o','s']
a.extend(b)
print("extending or adding one more list into a list: ",a)