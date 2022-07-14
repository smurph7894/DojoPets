from ninja import Ninja
from dog import Dog
from bird import Bird
from cat import Cat

first_ninja = {
    "first_name" : "Fred",
    "last_name" : "Sneeky"
}

happy = Ninja(first_ninja)

friendly_dog = {
    "name" : "Charles Richard",
}

CR = Dog(friendly_dog)

print(CR.name)
print(happy.first_name)

happy.add_pet(CR)

happy.feed().walk().bathe()
