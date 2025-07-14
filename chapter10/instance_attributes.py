class Employee:
    company = "Google" # Specific to Each Class
harry = Employee() # Object Instatiation
harry.company = "Youtube"  #Instance attribute
print(harry.company)

# Note:- Instance attributes take preference over the class attribute