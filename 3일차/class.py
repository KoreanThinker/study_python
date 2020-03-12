class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


std1 = Student("김", "19")
std2 = Student("최", "20")

print(std1.get_age())
print(std2.get_name())
