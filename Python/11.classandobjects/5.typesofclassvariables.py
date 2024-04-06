# self.a, self.roshan - if u use self. some var name means it is called instance variable.
# declare a var insided a class and outside function that is called class variable.


class phone:
    chrgrtyp="c type"  
    # class variable
    
    def __init__(self,br,pr):
        self.br=br
        self.pr=pr
        # instance variable
    
    def dis(self):
        print(self.br)
        print(self.pr)
        print(self.chrgrtyp)
        
        
ip=phone("iphone",86000)
ip.dis()