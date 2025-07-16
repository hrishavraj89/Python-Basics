class Employee:
    a = 1   #Class attribute
    
    @classmethod    #Using this method, it ignores the further crreated instance attributes and only print the value of class attribute
    def show(cls):  #In classmethod we use 'cls' instead of self.
        print(f"The class attribute of a is {cls.a}.")

Employee = Employee()
Employee.a = 0   #Instance attiribute
Employee.show()