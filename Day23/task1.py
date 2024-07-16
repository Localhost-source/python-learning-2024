# Take two numbers as input and add those numbers. Handle the possible exceptions.

def add_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

add_two_numbers()
