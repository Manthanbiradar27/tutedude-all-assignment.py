# Task 1: Create a Dictionary of Student Marks

students = {"Alice": 85,"Bob": 92,"Charlie": 78,"David": 90,"Eva": 88}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Sorry, no record found for student: {name}")


#Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_list = first_five[::-1]

print("Original List (1 to 10):", numbers)
print("First Five Elements:", first_five)
print("Reversed First Five Elements:", reversed_list)

