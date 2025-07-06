marks = int(input("Enter your marks"))

if(marks >= 90 and marks <= 100):
    print("Grade Ex")
if(marks >= 80 and marks <= 90):
    print("Grade A")
if(marks >= 70 and marks <= 80):
    print("Grade B")
if(marks >= 60 and marks <= 70):
    print("Grade C")
if(marks >= 50 and marks <= 60):
    print("Grade D")
if(marks >= 50 and marks <= 0):
    print("Grade F")

print("Your grade is", marks)