d = {}

name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter friend's name: ")
lang = input("Enter language: ")
d.update({name : lang})

print(d)

# If languages of two friends are same; what will happen to the program in problem
# 6?
# --- Same values can be entered twice in a dict, because update function only updates its value if key is same.