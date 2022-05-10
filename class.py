class Person:
    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
p1 = Person("John", "Smith", 45)
p2 = Person("Mary", "Jones", 32)
print(p1.first_name)
print(p2.age)