# class pepole:
#     height = 170
#     satiety = 50
# class worker(pepole):
#     satiety = 100
# class student(pepole):
#     satiety = 0
# mio=student()
# jojo=worker()
# print(jojo.satiety)
# print(jojo.height)

# class son:
#     height = 60
#     age = 1
# class grandfather:
#     height = 200
#     age = 60
# class parent(grandfather):
#     age = 40
# c4=son
# lary=parent()
# print(lary.age)
# print(lary.height)
# print(c4.age)
# print(c4.height)

# class hello_world():
#     hello = "Hello World"
#     _hello = "_Hello World"
#     __hello = "__Hello World"
#
#     def __init__(self):
#      self.world = "world"
#      self._world = "_world"
#      self.__world = "__world"
#     def printer(self):
#      print(self.hello)
#      print(self._hello)
#      print(self.__hello)
#      print(self.world)
#      print(self._world)
#      print(self.__world)
#
# class  hi(hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.world)
#         print(self._world)
# hello_world= hello_world()
# hi=hi()
#
# hello_world.printer()
#
# hi.hi_print()

# class computer:
#  def calculate(self):
#   print("calculate started")
#
# class display:
#     def display(self):
#         print("display started")
#
#
# class phone(display,computer):
#     pass
#
# phone = phone()
# phone =display()
# phone =computer()

# try:
#     print("ffg")
#     print(ytd)
#     print("gg")
# except:
#     print("oops error")

# try:
#    print("Hello World")
#    print("Hello again")
#    print(hkhjl)
# except:ZeroDivisionError
# print("ZeroDivisionError")
# except:NameError
# print("NameError")

try:
    x=int(input("Enter a number: "))
    res =10/x
    print(res)
except(ZeroDivisionError, ValueError)as error:
    print("помилка")