"""

class Person(object):
    def __init__(self, name, age, sex, hooby):
        self.name = name
        self.age = age
        self.sex = sex
        self.hooby = hooby
    
    def printtest(self):
        print ("%s, %s, %s, %s "%(self.name, self.age, self.sex, self.hooby))

p1 = Person("a", 10, "male", 1)
p1.printtest()


p2 = Person("b", 90, "female", 1)
p2.printtest()



class Person(object):
    def printtest(self, name, age, sex, hooby):
        self.name = name
        self.age = age
        self.sex = sex
        self.hooby = hooby
    
        print ("%s, %s, %s, %s "%(self.name, self.age, self.sex, self.hooby))

p1=Person("a", 10, "male", 1))
print(p1.printtest)
"""



