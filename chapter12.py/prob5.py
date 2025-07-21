# Store the multiplication tables generated in problem 3 in a file named Tables.txt

table = []
a = int(input("Enter a number:- "))
for i in range(1, 11):
    table.append(a*i)
    i += 1
with open('tables.txt', 'a') as f:
    f.write(f"Table of {a} : {str(table)} \n")