# Write a program to filter a list of numbers which are divisible by 5

numbers = {"23", "55", "60", "69", "20"}

numbers = [int(x) for x in numbers]   #Covert all the numbers to integers

div_by_5 = list(filter(lambda x: x % 5 == 0, numbers))

print(div_by_5)