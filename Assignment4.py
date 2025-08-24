# Task 1: Read a File and Handle Errors

def read_file(filename):
    try:
        with open(filename, "r") as file:

            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file("sample.txt")



#Task 2: Write and Append Data to a File

Take input from user and write to a file
user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data written to output.txt")

additional_input = input("Enter more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("Additional data appended to output.txt")


print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
