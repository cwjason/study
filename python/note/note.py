#import this (python编写规范)
####################################变量定义
value1 = 1
valueStr = "a"

####################################字符串
str_val = "this is a string"
str_val.title()     #开头大写
str_val.upper()     #全部大写
str_val.lower()     #全部小写
str_val.rstrip()    #去掉右边空白
str_val.lstrip()    #去掉左边空白
str_val.strip()     #去掉两边空白
str_val.split()     #通过空格划分字符串到列表
str_val.count('row') #在字符串中找row出现次数
str_val.replace("dog", "cat") #把dog 替换成cat
str(Integer)        #字符串转换
str_val = str_val + "!!!" #连接


####################################基本运算
#特殊 1 ** 2 == 1的平方

####################################列表
#定义
guest = ["tom", "lili", "mary"] #下标从0开始

#从-1开始是倒数开始取
#guest[-1] == "mary"

#表后面追加
guest.append("vinson")

#表指定位置插入
guest.insert(0, "mimi")

#删除表中数据
del guest[0]
#表末尾数据删除并返回
mem = guest.pop()
#表任意位置数据删除并返回
mem = guest.pop(2)
#表根据值删除元素，注：无返回
guest.remove("mary")

#组织列表，有序化
guest.sort()                #表排序，并修改原表
guest.sort(reverse=True)    #表排序并逆序，并修改原表
guest.reverse()             #反向排列

#sorted临时排序
sorted(guest)               #得到排序后的列表，不修改原表
sorted(guest, reverse=True)	#得到排序后且逆序后的列表，不修改原表

#获得表的长度
len(guest)

#################################### FOR
#注：for 语句内的语句需要添加缩进
for mem in guest:
    #TODO in for 
    #TODO in for
#TODO not in for


#################################### 值列表
#生成值列表range(开始值， 结束值)
range(1,6) #[1, 2, 3, 4, 5]
integerList = list(range(1, 6))

#指定步长
list(range(2, 11, 2)) #[2, 4, 6, 8, 10]

#基本统计函数
integerList = [1, 2, 3, 4, 5, 6]
min(integerList)
max(integerList)
sum(integerList)

#列表解析
squares = [value ** 2 for value in range(1, 11)]
#直接得到[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#处理列表部分元素（切片）
players = ["p1", "p2", "p3", "p4"]
players[0:2]    #从下标0，开始到下标2结束，得到p1, p2
players[:3]     #从头下标0开始
players[1:]     #从头下标1开始，到末尾
players[:]      #从头到尾
players[-3:]    #最后的3位元素

#遍历切片
players = ["p1", "p2", "p3", "p4"]
for p in players[-3:]:
    print(p)

#表复制
foods = ["apple", "banana", "orange"]
copy_foods = foods[:] # 复制表


#不可变的列表（元组）
#定义
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 150 赋值会报错


#################################### IF语句
players = ["player" + str(value) for value in range(1, 11)] #p1~p10
for p in players[:]:
    if p == "player1":
        print(p.upper())
    elif p == "player2":
        print(p.lower())
    else:
        print(p.title())

# 等于和不等于 
#   == !=
# 与和或
#   and or

#检查特定值是否包含在列表中
required_toppings = ['abc', 'aaa', 'ccc']
'abc' in required_toppings
# 不在表里面 not in

#确定表是不是空表
mytable = []
if mytable:
    print("this is not a empty table!")
else:
    print("this is a empty table!")

#字典
dict_table = {'color':'green', 'points':5}
dict_table['x_pos'] = 10
dict_table['y_pos'] = 25

#删除值
del dict_table['x_pos']

#遍历字典
for key, value in dict_table.items():
    print("Key:" + key)
    print("Val:" + str(value))

#获取所有键列表
for key in dict_table.keys():
    print(key.title())

#获取所有值列表
for value in dict_table.values():
    print(value.title())

#set集合(使表中元素是唯一的)
for value in set(dict_table.values()):
    print(value.title())

#嵌套
#字典列表,列表中存储字典
player_1 = {'name':'tom', 'age':5}
player_2 = {'name':'gen', 'age':6}
player_3 = {'name':'cot', 'age':7}

playerList = [player_1, player_2, player_3]

for player in playerList:
    print(player)

#字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese'],
}

for topping in pizza['toppings']:
    print("\t" + topping)

#################################### 用户输入input()原理
msg = input("tell me what you want!")
#python2.7 输入raw_input()
msg = raw_input("tell me:")

#################################### 求模运算符
#   4%3 == 1


#################################### while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

message = "tell me:"
active = True
while active:
    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    if message == 'quit':
        break
    else:
        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)



#################################### while 处理列表和字典
players = ['p1', 'p2', 'p3']
confirm_players = []

while players:
    p = players.pop()
    confirm_players.append(p)
    print("Verifying player:" + p.title())

for confirm_p in confirm_players:
    print(confirm_p.title())

#################################### 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#################################### 使用用户输入来填充字典
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


#################################### 函数定义
def myFunc():
    print('Hello World!')

myFunc()

#################################### 参数模式
#1 位置实参
def func(param1, param2):
    print(param1, param2)

func("param1", "param2")

#2 关键字实参
def func(param1, param2):
    print(param1, param2)

func(param1 = "param1", param2 = "param2")

#3 默认值
def func(param1, param2="param2"):
    print(param1, param2)

#################################### 返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', "hendrix")
print(musician)

#################################### 让实参可选
#传一个空字符串或默认值过去

#################################### 返回字典
def build_person(first_name, last_name):
    return {'first':first_name, 'last':last_name}




#################################### 传递列表
#注：会修改到原表
def greet_users(names):
    for name in names:
        msg = 'Hello,' + name.title() + '!'
        print(msg)

usernames = ['hahah', 'ty', 'margot']
greet_users(usernames)


#################################### 防止不修改到原表
def greet_users(names):
    for name in names:
        msg = 'Hello,' + name.title() + '!'
        print(msg)

usernames = ['hahah', 'ty', 'margot']
greet_users(usernames[:]) #传递副本


#################################### 传递任意数量实参
def make_pizza(*toppings):
    print(toppings)

#################################### 配合位置参数
def make_pizza(size, *toppings):
    print(toppings)

#################################### 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#################################### 函数导入
import module_name(py file)
module_name.function_name()

#能过逗号分隔函数名，可根据需要从模块中导入任意数量的函数:
from module_name import func_0, func_1, func_2

#通过as给模块改别名
import module_name as mn

#导入模块中的所有函数
from module_name import *



############################################################################################################终于面向对象了，类

#################################### 类的定义
class Dog(object):
    def __init__(self, name, age): #相当于构造
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


#################################### 类的继承
class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_car_model(self):
        return self.model.title()
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")

# 重写父类方法
#写C语言C++类似


#################################### 将实例用作属性
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
my_car.battery.describe_battery() #通过调用属性来调用对象方法


#################################### 导入类

#导入单个类
#from 文件名 import 类名

#导入所有类
#from 文件名 import * （不推荐）
'''
原因:
1 单个导入清晰知道导入哪些类
2 导入所有类有可能会引发同名类导致错误
'''

#################################### Python 标准库
#字典库，与普通的字典比，多了记录添加顺序
from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen']       = 'python'
favorite_languages['sarah']     = 'c'
favorite_languages['edward']    = 'ruby'
favorite_languages['phil']      = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#随机库
from random import randint
x = randint(1, 6)


#################################### 编写码风格
'''
    1 类名采用驼峰命名法，每个单词首字母大写，实例名和模块名采用小写，单词间加下划线
    2 对于每个类，类定义后面包含一个文档字符串进行类的说明
    3 导入模块时候，标准库放前面，和自己的模块隔一行做区分

'''


############################################################################################################文件和异常

#################################### 读取整个文件
# with 会保证打开文件正常使用的同时，在合适的时候自动将其关闭
'''
open 
param1:filename, 
param2:模式, 读取r, 写入w, 附加a ，读取写入模式r+，缺省是只读
'''
with open('car.py') as file_object:
    content = file_object.read()
    print(content.rstrip())

# 其它路径的文件，相对路径，windows 下用\ ，OSX 中用/
with open('text_files\my_file.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

# 逐行读取
with open('text_files\my_file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
with open('text_files\my_file.txt') as file_object:
    lines = file_object.readlines()

# 使用文件的内容
pi_string = ''
with open('text_files\my_file.txt') as file_object:
    lines = file_object.readlines()

    for line in lines:
        pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#如果想转为整形或浮点可以用float()或int()

# 包含一百万位的大型文件

pi_string = ''
with open('text_files\my_file.txt') as file_object:
    lines = file_object.readlines()

    for line in lines:
        pi_string += line.rstrip()

print(pi_string[:52] + "...")
print(len(pi_string))

#################################### 写入文件
filename = 'programing.txt'
with open(filename, "w") as file_object:
    file_object.write("I love programing.")


#################################### 异常
#try-except 代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#else代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("ok")

#处理FileNotFoundError异常
filename = 'alice.txt'

with open(filename) as file_object:
    contents = file_object.read()


#失败时一声不吭
try:
    print(5/0)
except ZeroDivisionError:
    pass # 什么都不做
else:
    print("ok")

#################################### 存储数据
#查看number_writer.py 和number_reader.py
#查看remember_me.py和greet_user.py


############################################################################################################测试代码
#查看test_name_function.py和name_function.py


############################################################################################################ 下载数据

#CSV文件格式
import csv

filename = 'csv\\test.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    print(header_row)


#json格式文件
import json

filename = 'json/test.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name    = pop_dict['Country Name']
        population      = pop_dict["Value"]
        print(country_name + ":" + population)


############################################################################################################ 使用AIP

#使用WEB API






