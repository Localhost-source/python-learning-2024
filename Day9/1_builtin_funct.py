# all()
# It takes iterable as a parameter and returns boolean result
# It takes only one parameter


vowels = ["a", "e", "i", "o", "u"]
result = all(vowels)
print(result)  # True

data = [1, 2, 3, 4, 0.0]
print(all(data))  # False


# any()
# It also takes iterable as a parameter and returns boolean
# It returns True of any one of the data is truthy
data = [1, 2, 3, 0]
result = any(data)
print(result)  # True


data = [False, 0, 0.0, None]
print(any(data))  # False

a = 1
b = 2
c = 10

if any([a > b, b > c]):  # syntactic sugar
    print("Something")


if a > b and b > c:
    pass

if all([a > b, b > c]):
    print("Something")