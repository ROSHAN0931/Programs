# Set
# 1.do not allow duplicate, duplicate values will be removed
# 2.any type of data can be sorted
# 3.we cannot modify it but we can add or remove items
# 4.sets are unordered

a={1,1,2,3,4}
print("stes are : ",a) #{1,2,3,4}
a.add(23)
print("after adding : ",a)
a.remove(23)
print("after removing : ",a)
a.update("roshan")
print("it will update the set in different order : ",a)
a.pop()
print("it will remove first item : ",a)