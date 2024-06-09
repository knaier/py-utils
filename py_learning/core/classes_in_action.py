# Import the dogs frm the classes module
from classes import Dog, Grayhound as Grayhound

willie = Dog("Willie", 2)

print(f"My dogs name is {willie.name} and is {willie.age} years old")

willie.sit()
willie.roll_over()


fred = Grayhound("Fred", 1)
print(f"My dogs name is {willie.name} and is {willie.age} years old")

fred.sit()
fred.roll_over()
