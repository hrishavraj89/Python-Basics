# Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:

    def __init__(self, n):
        self.number = n

    def square(self):
        print(f"The square is {self.number*self.number}")

    def cube(self):
        print(f"The cube is {self.number*self.number*self.number}")

    def squareroot(self):
        print(f"The square root is {self.number**(1/2)}")

    @staticmethod
    def greet():
        print("Thank You!")

a = Calculator(int(input("Enter a number:- ")))
a.square()
a.cube()
a.squareroot()
Calculator.greet()