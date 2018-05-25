from car import Car
from electric_car import ElectricCar

my_new_car = Car("audi", "a4", 2016)

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_electric_car = ElectricCar("tesla", "model s", 2016)
my_electric_car.show_car_info()