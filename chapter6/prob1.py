a1 = int(input("Enter first number"))
a2 = int(input("Enter first number"))
a3 = int(input("Enter first number"))
a4 = int(input("Enter first number"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is ",a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is ",a2)
if(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is ",a3)
if(a4>a2 and a4>a3 and a4>a1):
    print("Greatest number is ",a4)

else: print("not a valid number")