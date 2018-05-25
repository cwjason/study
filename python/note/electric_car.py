from car import Car

class Battery(object):
    def __init__(self, battery_size = 70):
        print("")
        self.battery_size = battery_size
    def describe_battery(self):
        print("this is a electricity")
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")
    def show_car_info(self):
        print("this is a electricity car!")