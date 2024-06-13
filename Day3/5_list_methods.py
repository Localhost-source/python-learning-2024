# append()
# extend()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()
# insert()


# append()
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]


# extend()
# extend() method takes iterable as a parameter
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)  # [1, 2, 3, 4, 5, 6]


# remove()
a = [1, 2, 3, 4, 5]
a.remove(3)
print(a)  # [1, 2, 4, 5]
# a.remove(100) # ValueError

vowels = ["a", "e", "i", "o", "u", "o"]
vowels.remove("o")
print(vowels)  # ["a", "e", "i", "u", "o]


# pop()
# pop() method alters the list and it also returns the popped item as a returntype.
vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop()
print(vowels)  # ["a", "e", "i", "o"]
print(result)  # "u"

result = vowels.pop(2)
print(vowels)  # ["a", "e", "o"]
print(result)  # i

# result = vowels.pop(100)  # Error