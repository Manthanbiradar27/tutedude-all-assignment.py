num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"


print("\nResults:")
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division





**Task 2: Create a Personalized Greeting**


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


full_name = first_name + " " + last_name


print("\nHello, " + full_name + "! Welcome to Python programming.")