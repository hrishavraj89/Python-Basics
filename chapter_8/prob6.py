# Write a python function which converts inches to cms

def inch_to_cms(n):
    return n * 2.54

n = int(input("Enter the length in Inches:- "))
print(f"{inch_to_cms(n)} Inches")