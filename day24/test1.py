def addition(a, b):
    return a + b

A = 10

print(__name__, "<-------------")  # It is the name of module
if __name__ == "__main__":
    result = addition(2, 3)
    print(result)  # 5
