# Define conversion functions

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15


# Main program
print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(f))

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Kelvin:", celsius_to_kelvin(c))

else:
    print("Invalid choice")
