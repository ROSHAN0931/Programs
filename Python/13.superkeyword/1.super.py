class a():
    def __init__(self):
        print("A")
    def dis(self):
        print("ur in class a")
    
class b(a):
    def __init__(self):
        super().__init__() #it will indicate to parent class
        print("B")
    def dis(self):
        print("ur in class b")
        
roshan=b()


class a():
    def __init__(self):
        print("A")
    def dis(self):
        print("ur in class a")
    
class b():
    def __init__(self):
        super().__init__()
        print("B")
    def dis(self):
        print("ur in class b")
        
class c(b,a):  #left parent will be called first
    def __init__(self):
        super().__init__() 
        print("C")
    def dis(self):
        print("ur in class c")
        
roshan=c()
