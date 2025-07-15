# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

h = Programmer("Hri", "24", "200000")
print(h.name, h.age, h.salary)

h = Programmer("Doraemon", "25", "100000")
print(h.name, h.age, h.salary)