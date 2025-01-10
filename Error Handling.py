def divide_number():
    try:

        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))

        result = num1 / num2
        print(f"The result {result}.")

    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    except ValueError:
        print("Please enter valid number.")

    except Exception as limon:

        print(f"An unexpected error occurred: {limon}")
divide_number()
