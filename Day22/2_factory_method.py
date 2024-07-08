
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_age_from_year(name, birth_year):
    current_year = 2024
    age = current_year - birth_year
    return Person(name, age)

p1 = Person("Alex", 24)
print(p1.age)  # 24

p2 = get_age_from_year("Jon", 1992)
print(p2.age)  # 32
