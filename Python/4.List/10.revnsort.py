a=[1,2,4,3,5]
print("before reversing : ",a)
a.reverse() #reversing a list
print("after reversing : ",a)
a.sort(reverse=False)
print("after sorting: ",a)

b=["red","blue","orange","black"]
b.sort(reverse=True)
print(b)

#output
'''before reversing :  [1, 2, 4, 3, 5]
after reversing :  [5, 3, 4, 2, 1]
after sorting:  [1, 2, 3, 4, 5]
['red', 'orange', 'blue', 'black']'''