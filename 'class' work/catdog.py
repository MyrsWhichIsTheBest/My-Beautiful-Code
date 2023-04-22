class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

    def speak(self):
        print("WAP!")


class Cat(Pet):
    def speak(self):
        print("Meow!")


class Dog(Pet):
    def speak(self):
        print("Woof!")

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old")


class Snake(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old and my skin color is: {self.color}.")


c = Cat("Felix", 99)
c.show()
c.speak()
d = Dog("Ganymede", 2)
d.show()
d.speak()
p = Pet("Posai", 8)
p.show()
p.speak()
s = Snake("Snak", 10000, "Rojo")
s.show()
s.speak()
