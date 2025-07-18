# Write a python program using function to convert Celsius to Fahrenheit.
def temperature(a):
    return a * 9/5 + 32

a = int(input("Enter the temperature in celcius:- "))
print(f"Temperature in Fahrenheit is {temperature(a)}")