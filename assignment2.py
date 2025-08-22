#task 1:

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")


#task 2:


total_sum = 0


for num in range(1, 51):
    total_sum += num


print("The sum of numbers from 1 to 50 is:", total_sum)
