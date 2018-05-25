
'''
guest = []
guest.append("father")
guest.append("mother")
guest.append("brother")

#guest.sort(reverse=True)
#pprint(guest)
#pprint(sorted(guest))
#pprint(sorted(guest, reverse=True))
#pprint(guest)
#p#pprint(len(guest))


#pfor mem in guest:
	#print(mem.title() + ", that was a great trick!")
	#print("i can't wait to see your next trick, " + mem.title())


#print("thank you, every one. That was a great magic show!")


myT = ['1', '2', '3']
#pfor t in myT:
	#print(t)

myList = list(range(2, 11, 2))

#pfor num in myList:
	#print("this is my lucky num:" + str(num))


#print(range(1,5))

sequares = [value ** 2 for value in range(1, 6)]
print(sequares)

for p in sequares[-3:]:
	print(p)

foods = ["apple", "banana", "orange"]
copy_foods = foods[:]
print(foods)
print(copy_foods)

foods.append("ice cream")
copy_foods.append("hotdog")
print(foods)
print(copy_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 150

foods = ("piz", "ice cream", "hot dog")

for food in foods[:]:
    print(food)

players = ["player" + str(value) for value in range(1, 11)]
print(players)
for p in players[:]:
    if p == "player1":
        print(p.upper())
    else:
        print(p.title())

required_toppings = ['abc', 'aaa', 'ccc']
print('bbb' in required_toppings)

mytable = []
if mytable:
    print("this is not a empty table!")
else:
    print("this is a empty table!")
'''

'''
dict_table = {'color':'green', 'points':5}
print(dict_table['color'])
print(dict_table['points'])

dict_table['x_pos'] = 10
dict_table['y_pos'] = 25


del dict_table['x_pos']
print(dict_table)

for key, value in dict_table.items():
    print("Key:" + key)
    print("Val:" + str(value))


player_1 = {'name':'tom', 'age':5}
player_2 = {'name':'gen', 'age':6}
player_3 = {'name':'cot', 'age':7}

playerList = [player_1, player_2, player_3]

playerList = []
for player_num in range(30):
    newPlayer = {'name':'jason' + str(player_num), 'age':28}
    playerList.append(newPlayer)

for player in playerList[:5]:
    print(player)

print("total :" + str(len(playerList)))
'''

'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

message = ""
while message != 'quit':
    message = raw_input("tell me what to do!:")
    if message != "quit":
        print(message)
'''

'''
players = ['p1', 'p2', 'p3']
confirm_players = []

while players:
    p = players.pop()
    confirm_players.append(p)
    print("Verifying player:" + p.title())

for confirm_p in confirm_players:
    print(confirm_p.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

polling_active = True
while polling_active:
    name = raw_input("\n what is your name?")
    response = raw_input("Which mountain would you lick to climb someday?")

    responses[name] = response

    repeat = raw_input("Would you like to let another person respond?(y/n)")
    if repeat == 'n':
        polling_active = False
print("\n ------- Poll Result -----")
for name, response in responses.items():
    print(name + "would like to climb " + response + ".")
'''

'''
def myFunc():
    print('Hello World!')

myFunc()


def myParamFunc(name):
    print(name)


myParamFunc("jason")

def func(param2, param1):
    print(param1, param2)

func(param1 = "param1", param2 = "param2")

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', "hendrix")
print(musician)
'''

'''
def greet_users(names):
    for name in names:
        msg = 'Hello,' + name.title() + '!'
        print(msg)

usernames = ['hahah', 'ty', 'margot']
greet_users(usernames)

def make_pizza(*toppings):
    for value in toppings[:]:
        print(value)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''


'''
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
'''

#import pizza

#pizza.make_pizza(15, 'seafood', 'cheeze')

#from pizza import make_pizza
#make_pizza(15, 'seafood', 'cheeze')

#import pizza as p
#p.make_pizza(15, 'seafood', 'cheeze')

#from pizza import *
#make_pizza(15, 'seafood', 'cheeze')

'''
import dog

my_dog = dog.Dog("willie", 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
'''

'''
import car

my_car = car.Car("subaru", "outback", 2013)
print(my_car.get_descriptive_name())


my_tesla = car.ElectricCar("tesla", "model", 2016)
my_tesla.describe_battery()
my_tesla.show_car_info()
'''

'''
class Car(object):
    def __init__(self):
        print("")
class Battery(object):

    def __init__(self, battery_size = 70):
        print("")
        self.battery_size = battery_size
    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "=kWh battery." )
class ElectricCar(Car):
    def __init__(self):
        super(ElectricCar, self).__init__()
        self.battery = Battery()

my_car = ElectricCar()
my_car.battery.describe_battery()
'''

'''
class Restaurant(object):
    def __init__(self):
        print("this is a Restaurant!")

    def showMenu(self):
        print("show Restaurant menu!")

class IceCreamStand(Restaurant):
    def __init__(self, *menuList):
        super(IceCreamStand, self).__init__()

        self.menuList = menuList

    def showMenu(self):
        for item in self.menuList:
            print(item)

my_stand = IceCreamStand("redIce", "blueIce", "greenIce")
my_stand.showMenu()
'''
'''
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen']       = 'python'
favorite_languages['sarah']     = 'c'
favorite_languages['edward']    = 'ruby'
favorite_languages['phil']      = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


from random import randint

x = randint(1, 6)
while x != 1:
    x = randint(1, 6)
    print(x)

with open('text_files\my_file.txt') as file_object:
    content = file_object.read()
    #print(content)

with open('text_files\my_file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())


with open('text_files\my_file.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)

pi_string = ''
with open('text_files\my_file.txt') as file_object:
    lines = file_object.readlines()

    for line in lines:
        pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

pi_string = ''
with open('text_files\my_file.txt') as file_object:
    lines = file_object.readlines()

    for line in lines:
        pi_string += line.rstrip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = raw_input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appears in the first million digits of pi!")
    '''
'''
message = "l really like dog"
print(message.replace('dog', 'cat'))



guest_name = raw_input("Please input you name!")
filename = 'programing.txt'
with open(filename, "w") as file_object:
    file_object.write(guest_name + " I love programing.\n")
    #file_object.write("I love creating new games.\n")

'''

with open(filename) as file_object:
    contents = file_object.read()
