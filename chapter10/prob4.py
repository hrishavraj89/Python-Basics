# Add a static method in problem 2, to greet the user with hello

class Calculator:

    @staticmethod
    def greet():
        print("Hello!")

    def __init__(self, n):
        self.number = n

    def square(self):
        print(f"The square is {self.number*self.number}")

    def cube(self):
        print(f"The cube is {self.number*self.number*self.number}")

    def squareroot(self):
        print(f"The square root is {self.number**(1/2)}")


Calculator.greet()
a = Calculator(int(input("Enter a number:- ")))
a.square()
a.cube()
a.squareroot()