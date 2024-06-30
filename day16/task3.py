"""
“Python + is + an + awesome + language”.
Split the given string to get a list and join to get another string
“Python is an awesome language”
"""

s = "Python + is + an + awesome + language"

x = s.split(" + ")  # []
result = " ".join(x)  # Here list elements are joined by " "
print(result)  # "Python is an awesome language"
