# Wap a program to check whether an input number is odd or even.

num = int(input("Enter a number"))

if num % 2:
    print(f"{int} is even")
else:
    print(f"{int} is odd")


# Write a py code to take three numbers input and print the greatest number.

num1 = int(input("Enter the number"))
num2 = int(input("Enter the number"))
num3 = int(input("Enter the number"))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the greatest")
    else:
        print(f"{num1} is not the greatest")
elif num3 > num1:
    if num3 > num2:
        print(f"{num3} is the greatest")
    else:
        print(f"{num3} is not the greatest")

else:
    print("num2 is greatest")


