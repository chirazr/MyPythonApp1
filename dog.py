class smallAnimal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk (self):
        print (f" {self.name} walk")


# simple code 

class Dog:

    def walk(self):
        print("walk")

# heritage 
class Dog(smallAnimal):
    pass

dog = Dog()
dog.walk()



# function
class Dog(smallAnimal):
    def special_speak(self):
        return " the dog speak "

dog = Dog("lulus",2)
dog.walk()
print (dog.special_speak())


