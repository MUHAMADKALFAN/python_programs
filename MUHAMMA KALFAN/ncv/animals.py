class Animal:
    def  speak(self):
        print("all animals has different methods")

class Dog(Animal):
    def speak(self):
        print("dogs says Woof!")

class Cat(Animal):
    def speak(self):
        print("cat says Meow!")

# animal=Animal()
# animal.speak()

dog=Dog()
dog.speak()

cat=Cat()
cat.speak()