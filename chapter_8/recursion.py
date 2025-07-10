# To find the fatorial of any number entered by the user.
# Factorial = n X (n-1) X ..... X 3 X 2 X 1
# Factorial of 1 = 1
# Factorial of 0 = 1 

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number:- "))
print(f"The factorial of the given number is {factorial(n)}")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# n = int(input("Enter a number:- "))
# print(f"The factorial of the given number is {factorial(n)}")
