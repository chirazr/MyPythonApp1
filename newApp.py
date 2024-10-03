
# class ClassName:
#    satement 

class Car:
    def __init__(self,color,name,year,energy):
        self.color = color
        self.name = name
        self.year = year
        self.energy = energy
    



    def go_back(self):
        print ("the car go back")

    def go_forward(self):
        print ("the car go forward")



Car1 = Car()
Car1.go_back()
Car1.color = "red"
Car1.name = "kia"
print (Car1.name)

car1 = Car("red","kia",2018,"benz")
print (Car1.name)




