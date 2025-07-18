# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:
    def __init__(self, real_part, img_part):
        self.real_part = real_part
        self.img_part = img_part

    def __add__(self, other):
        return Complex(self.real_part + other.real_part, self.img_part + other.img_part)
    
    def __mul__(self, other):
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real = self.real_part * other.real_part - self.img_part * other.img_part
        img = self.real_part * other.img_part + self.img_part * other.real_part
        return Complex(real, img)

    def __str__(self):
        return f"{self.real_part} + {self.img_part}i"

# Example
a = Complex(1, 2)
b = Complex(3, 4)

sum_result = a + b
mul_result = a * b

print("Sum =", sum_result)       # Output: 4 + 6i
print("Multiplication =", mul_result)  # Output: -5 + 10i 