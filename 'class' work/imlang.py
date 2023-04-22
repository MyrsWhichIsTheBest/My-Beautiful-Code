class tugBoat:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def deet(self):
        return f"wait that's a dog named {self.name} who's {self.age} years old and has {self.colour} fur!"

    def change_age(self, age):
        self.age = age


dog1 = tugBoat("Dodie", 4, "brown")
dog2 = tugBoat("Mackie", 10, "oreo")

print(tugBoat.deet(dog1))
print(tugBoat.deet(dog2))

dog1.change_age(5)
dog2.change_age(81000)

print(tugBoat.deet(dog1))
print(tugBoat.deet(dog2))
