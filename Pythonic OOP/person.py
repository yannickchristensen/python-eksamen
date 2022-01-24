class Person:
    isHuman = True
    def __init__(self, *args):
        if len(args) == 2:
            self.name = args[0]
            self.age = args[1]


    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


# Objects
a = Person('John',22)
b = Person('John',22)
print(a==b)
c = b
print(c==b)

print(isinstance(a, str))
print(isinstance(a, Person))
print(isinstance(a, object))

# Access
a.introduce()
print(a.name,a.age,a.isHuman)


# Inheritance
class Student(Person):
    def __init__(self, name, age, field):
        super().__init__(name, age)
        self.field = field

    def formalIntroduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old and I study {self.field}")



s = Student('Sally', 22, 'Psychology')
s.introduce()
s.formalIntroduce()

print(isinstance(s, Student))
print(isinstance(s, Person))

