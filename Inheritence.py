class Person:
  def __init__ (self, name,place):
     self.name = name
     self.place = place
  def info(self):
    return self.name, self.place
class Employee(Person):
    pass
a = Employee("dipendra","nepalgunj")
print(a.info())


class Dog:
 def eat(self):
      print("Dog is eating")
class Animal(Dog):
 def display(self):
    print("display")
a=Animal()
a.display()
a.eat()
class Hari:
    def read(self):
        print("Hari is reading")
class Ram:
    def write(self):
        print("Ram is reading")
class person(Hari, Ram):
    pass
c = person()
c.read()
c.write()