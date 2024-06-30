"""
Write a Python program to create a dictionary from a string. Track the count of the letters from the string.
Input = “broadway”
Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}
"""


def get_char_count(data):
    """
    :param data: string
    :return: dictionary with count of each elements
    """
    result = {}
    for each in data:  # broadwayayayayab
        if each in result:
            result[each] += 1
        else:
            result[each] = 1  # {"b": 1, "r": 1, "o": 1, "a": 1, "d": 1}

    return result


d = input("Enter a string ")
r = get_char_count(d)
print(r)  # {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}

