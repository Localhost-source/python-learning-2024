# •Take two numbers input and divide a number by another number. Handle the possible exceptions has context menu...

def divide_two_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
    except ZeroDivisionError:
        print("Error: Please dont provide 0 at denominator.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divide_two_numbers()
