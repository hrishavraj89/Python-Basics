# 3. A list contains the multiplication table of 7. write a program to convert it to vertical
# string of same numbers

a = int(input("Enter a number:- "))

table = [a * i for i in range(1, 11)]

vertical_string = "\n".join(str(num) for num in table)
print(vertical_string)
