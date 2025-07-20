# Write a program to print third, fifth and seventh element from a list using enumerate
# function.

fruits = ["Apple", "Mango", "Banana", "Watermelon", "Pear", "Guava", "Orange", "Grapes"]
for index, list in enumerate(fruits):
    if index == 2 or index == 4 or index == 6:
        print(list)