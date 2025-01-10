
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

sum_even = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of all even numbers from 1 to {number} is {sum_even}.")
