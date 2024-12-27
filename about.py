class Car :
    def __init__(s,brand,speed):
        s.brand = brand
        s.speed = speed
    def increase(s,value):
        s.speed += value
    def displaySpeed(s):
        print(s.brand + " is runnimg at ",s.speed)
car1 = Car('Tesla',100)
car1.displaySpeed()
car1.increase(50)
car1.displaySpeed()

class Dog :

    pass