# __str__() method to print the vector as follows:
#  7i + 8j +10k 

class Vector:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k

    def show(self):
        result = f"{self.x}i + {self.y}j + {self.k}k"
        return result
    
    def __str__(self):
        return f"The vector is {self.x}i + {self.y}j + {self.k}k"
    
a = Vector(7, 8, 10)
print(a.show())