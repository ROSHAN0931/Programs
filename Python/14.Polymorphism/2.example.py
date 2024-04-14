# Create class Animal with a method that prints "animal makes a sound". Create a derived class Dog
# that inherits from animal class and overrides the sound() method to print "Dog barks". Create 
# another derived class Bird that inherits from animal and overrides the sound method to print
# "Birds sing".

class animal():
    def sound(self):
        print("animal makes sound") 

class dog(animal):
    def sound(self):
        print("Dog barks")
        
class bird(animal):
    def sound(self):
        print("birds sing")        

b1=bird()
b1.sound()