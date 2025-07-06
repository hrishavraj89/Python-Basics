a = int(input("Enter your age"))

if(a>=18):
    print("You are an adult")

elif(a<0):
    print("You are a child")

elif(a==0):
    print("Invalid age")

else:
    print("You are below the age of concent")

print("Thanks!")

# if the condition me in the 'if' is true then 'if' condition will execute.
# the compiler will first check the if statement, if false, the execute the next elif statement.
# if that is also false, then it will check the next elif statement and lastly, the else statement will be excuted if all are False.