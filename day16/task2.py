"""
Vowel check
"""


# def is_vowel(char):
#     if char.lower() in ('a', 'e', 'i', 'o', 'u'):
#         return True
#     else:
#         return False
#
#
# chk = input("Enter Character to check: ")
#
# result = is_vowel(chk)

# print(result)


data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

vowels = filter(lambda x: x in ["a", "e", "i", "o", "u"], data)

print(list(vowels))



data = [4, 5, 10, 12, 11]
result = filter(lambda x: x - 10, data)
print(list(result))  # [4, 5, 12, 11]
