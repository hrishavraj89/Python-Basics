# Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

table = []
a = int(input("Enter a number:- "))
for i in range(1, 11):
    table.append(a*i)
    i += 1
print(table)