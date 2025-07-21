# Write a program to find the maximum of the numbers in a list using the reduce
# function.

from functools import reduce

numbers = {"23", "55", "60", "69", "20"}

def greater(a, b):
    if (a > b):
        return a
    return b    #No need to use else statements if there is no elif.

print(reduce(greater, numbers))