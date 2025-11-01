


class Car:
    def __init__(self,brand,year):
        self.__brand = brand
        self.year = year
    def get_brand(self):
        return self.__brand + "!"
    def bhegu(self):
        return f"{brand}-{year}"
    def fuel_type(self):
        return "Petrol or disel"
    @staticmethod
    def general_description():
        return "Cars are used to drive"
class Ecar(Car):
    def __init__(self,brand,year,battery):
        super().__init__(brand,year)
        self.battery = battery
    def fuel_type(self):
        return "Electric type"

brand = input("Enter a brand name: ")
year = int(input("Enter year of oppening of brand: "))
battery = input("Enter battery size: ")

my_car = Ecar(brand,year,battery)
#print(my_car.brand)#File "<main.py>", line 19, in <module>
#AttributeError: 'Ecar' object has no attribute 'brand',by using private method
print(my_car.get_brand())
print(my_car.year)
print(my_car.bhegu())
print(my_car.battery)
print(my_car.fuel_type())

general_Car = Car(brand,year)#polymorphism
print(general_Car.fuel_type())
print(Car.general_description())#staticmethods part of decorators
print(Ecar.general_description())#It can be called by child class also

class Engine:
    def start(self):
        return "Engine started"
class Battery:
    def charge(self):
        return "Battery charging"

class HybridCar(Car,Engine,Battery):
    def __init__(self,brand,year,battery):
        Car.__init__(self,brand,year)
        self.battery = battery

my_hybrid = HybridCar(brand,year,battery)
print(my_hybrid.get_brand())
print(my_hybrid.start())
print(my_hybrid.charge())
