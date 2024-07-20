# If a function is called within the definition of the same function then such function
# is called recursive function


# Infinite Recursion
# In such case the code breaks after reaching the maximum recursion depth (~1000)
# def message():
#     print("Hello World")
#     message()
#
# message()


a = 0
def counter():
    global a
    print(a)
    a += 1
    if a <= 10:
        counter()

counter()


# Find the factorial of 5 using:
# i. for loop
# ii. reduce
# iii. recursion

from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 6))
print(result)  # 120


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


result = factorial(5)
print(result)  # 120


# n * factorial(n-1)
# 5 * factorial(4)  # 5 * 24 = 120
# 4 * factorial(3)  # 4 * 6 = 24
# 3 * factorial(2)  # 3 * 2 = 6
# 2 * factorial(1)  # 2 * 1 = 2
# 1 * factorial(0)  = 1 * 1 = 1