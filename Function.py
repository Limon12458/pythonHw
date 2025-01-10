def sum_even_odd(numbers):
    sum_even = 0
    sum_odd = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even, sum_odd

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum_even, sum_odd = sum_even_odd(numbers)

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")
