# meta class
class newsample():
    pass

newobj = newsample()
print(type(newobj))
print(type(newsample))

# Building class with metaclass
# player is a class

Player = type('Player', (Team,), {})

# Adding attributes and methods/functions
class Player:
    def __init__(self,name,age):
        self.name = name
        self.age = 23
        self.number = 5
def init(self,name,age):
    self.name = name
    self.age = 25
    self.number = 8

Player = type('Player', (), {'__init__': init})
print(Player)
