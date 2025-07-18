# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:
    def __init__(self, real_part, img_part):
        self.real_part = real_part
        self.img_part = img_part

    def __add__(self, sum):
        return Complex(self.real_part + sum.real_part, self.img_part + sum.img_part)

    def __str__(self):
        return f"{self.real_part} + {self.img_part}i"
    
a = Complex(1, 2)
b = Complex(3, 4)
result = a+b
print(result)