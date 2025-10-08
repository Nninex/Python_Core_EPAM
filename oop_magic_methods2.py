'''
Magic methods. Task 2 
Create a hierarchy out of birds. Implement 4 classes: * class Bird with an attribute name and methods fly and walk. * class FlyingBird with attributes
name, ration, and with the same methods. ration must have a default value. Implement the method eat which will describe its typical ration. * class
NonFlyingBird with same characteristics but which obviously without attribute fly. Add the same “eat” method but with other implementation
regarding the swimming bird tastes. * class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which “eat” method you inherit. 
Implement str() function call for each class. 
Example: ```python  b = Bird(“Any”) b.walk() “Any bird can walk” 
p = NonFlyingBird(“Penguin”, “fish”) 
p.swim() “Penguin bird can swim” 
p.fly() AttributeError: ‘Penguin’ object has no attribute ‘fly’ p.eat() “It eats mostly fish” 
c = FlyingBird(“Canary”) 
str© “Canary bird can walk and fly” c.eat() “It eats mostly grains” 
s = SuperBird(“Gull”) 
str(s) “Gull bird can walk, swim and fly” s.eat() “It eats mostly fish” ``` 
Have a look at the mro method or the attribute __mro__ of your last class

'''


class Bird:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name} bird can walk"

    def walk(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = "grains"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can walk and fly"

    def fly(self):
        return f"{self.name} bird can fly"

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird(Bird):
    def __init__(self, name: str, ration: str = "fish"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can swim"

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name: str):
        FlyingBird.__init__(self, name, ration="fish")
        NonFlyingBird.__init__(self, name, ration="fish")

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"

    def swim(self):
        return f"{self.name} bird can swim"
