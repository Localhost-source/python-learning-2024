"""
WAP to sum all the digits of a three-digit number
input: 573
output: 15
"""


def sum_of_digits(number):
    digits = str(number)
    
    digit_sum = int(digits[0]) + int(digits[1]) + int(digits[2])
    
    return digit_sum

number = 573

print(sum_of_digits(number))  
