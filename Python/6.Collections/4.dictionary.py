# Dictionary
# 1.do not allow duplicate,duplicate eill overwrite existing value
# 2.any type of data can be sorted

a={"name":"roshan","age":1,"location":"ooty","place":["ooty","cbe","denalai"]}
print(a)
print("value of a in dictionary name:",a["name"])
print("my age is :",a["age"])
print(a)
print("it will print only keys: ",a.keys()) #name,age,location,place
print("only values: ",a.values()) #roshan,23,ooty....
a["age"]=23 # or a.update({"age":23})
print("after modify: ",a)
a["color"]="red" #this will add in the last
print("will be adding in last: ",a)
a.pop("place")
del a["name"]
print("after removing: ",a)
a.clear()
print("dict will be empty: ",a)