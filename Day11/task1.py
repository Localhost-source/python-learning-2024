# store 0-50 even numbers in a list.

result = []
for n in range (51):
    if n % 2 == 0:
        result.append(n)
        print(result)