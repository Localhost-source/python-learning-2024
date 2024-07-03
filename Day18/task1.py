"""
Check whether the input number is prime or composite.
"""

def is_prime(n):
    if n <= 1:
        return False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

def check_prime_or_composite(num):
    if num <= 1:
        return "Neither prime nor composite"
    if is_prime(num):
        return "Prime"
    else:
        return "Composite"

number = int(input("Enter a number: "))
result = check_prime_or_composite(number)
print(f"The number {number} is {result}.")
