"""
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

"""


def get_unique(lst):
    result = []
    for each in lst:
        if each not in result:
            result.append(each)
    return result


data = [1, 2, 3, 3, 3, 3, 4, 5]
res = get_unique(data)
print(res)


def get_unique(lst):
    result = []
    [result.append(each) for each in lst if each not in result]
    return result


data = [1, 2, 3, 3, 3, 3, 4, 5]
res = get_unique(data)
print(res)



"""
15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list [5, 7, 9]
"""


def add_two_lists(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Invalid length of two lists"
    result = []
    for index, value in enumerate(lst1):
        s = value + lst2[index]
        result.append(s)
    return result

l1 = [1, 2, 3]
l2 = [4, 5, 6]

r = add_two_lists(l1, l2)
print(r)  # [5, 7, 9]



data = zip(l1, l2)
print(list(data))


def add_two_lists(lst1, lst2):
    iterable = zip(lst1, lst2)   # [(1, 4), (2, 5), (3, 6)]
    result = map(lambda x: sum(x), iterable)
    return list(result)


res = add_two_lists(l1, l2)
print(res)
