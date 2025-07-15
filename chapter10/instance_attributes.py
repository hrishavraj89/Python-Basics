class Employee:
    company = "Google" # Specific to Each Class(class attribute)
harry = Employee() # Object Instatiation
harry.company = "YouTube"   #Instance attribute
harry.age = "24"   #Instance attribute
print(harry.company, harry.age)

# Note:- Instance attributes take preference over the class attribute
# Here company is a class attribute and age is instance attribute!