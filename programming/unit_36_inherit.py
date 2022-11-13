#연습
class AdvancedList(list):
    def replace(self, a, b):
        while a in self:
            self[self.index(a)] = b
x = AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1, 100)
print(x)


#심사
class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Fly:
    def fly(self):
        print('날다')

class Bird(Animal, Wing, Fly):
    def issubclass(self):
        print(Bird)

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))