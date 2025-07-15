class Employee:
    language = "English"    #This is a class attribute
    salary = "20000"
    
    def __init__(self, name, age, course):   #methods which start with "__" are known as Dunder Methods.
        self.name = "Hri"   #init method is automatically called when an object is created.
        self.age = "30"
        self.course = "BTech"
        print("Init function is a constructor which is automatically called when the object is passed")


    company = "Google"
    def getsalary(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod    #Sometimes, we need a function which does not use the self parameter.
    def greet():     #We define it by using the @staticmethod.
        print("Hello, Everyone!")

harry = Employee("Hri", "24", "AI & ML")

harry.getsalary()
harry.greet()
print(harry.name, harry.age, harry.course)

# hri = Employee()