class Animal:
    def  speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Cow(Animal):
    def speak(self):
        return "Moo!"
Dog=Dog()
Cat=Cat()
Cow=Cow()
print("Dog says:-",Dog.speak())
print("Cat says:-",Cat.speak())
print("Cow says:-",Cow.speak())
