# # Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.


class Employee:
    salary = 200
    increment = 20

    @property
    def salary_after_inc(self):
        return (self.salary + self.salary * (self.increment / 100))
    
    @salary_after_inc.setter
    def salary_after_inc(self, salary):
        self.increment = ((salary / self.salary) -1) * 100


e = Employee()
e.salary_after_inc = 250
print(e.increment)
    