# single inheritance
print("Single")
class dad():
    def phone(self):
        print("dads phone")

class son(dad):
    def lap(self):
        print("sons lap")

roshan=son()
roshan.lap()
roshan.phone()

# Multiple inheritance
print("Multiple")
class dad():
    def phone(self):
        print("dads phone")

class mom():
    def sweet(self):
        print("Moms sweet")

class son(dad,mom):
    def lap(self):
        print("sons lap")

roshan=son()
roshan.lap()
roshan.phone()
roshan.sweet()

# Multilevel inheritance
print("Multilevel")
class grand():
    def phone(self):
        print("grand phone")

class dad(grand):
    def money(self):
        print("Dads money")

class son(dad):
    def lap(self):
        print("Sons lap")
    
roshan=son()
palani=dad()

roshan.lap()
roshan.money()

palani.money()
palani.phone()

roshan.phone()

# Hierarchical Inheritance
print("Heirarchical")
class dad():
    def money(self):
        print("Dads money")
        
class land():
    def imp(self):
        print("important land")
        
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

roshan=son1()
roshan.money()
roshan.imp()
