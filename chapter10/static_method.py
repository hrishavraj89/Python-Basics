class Employee:
    company = "Google"
    def getsalary(self):
        print("Salary is not there")

    @staticmethod    #Sometimes, we need a function which does not use the self parameter.
    def greet():     #We define it by using the @staticmethod.
        print("Hello, Everyone!")

harry = Employee()

harry.getsalary()
harry.greet()