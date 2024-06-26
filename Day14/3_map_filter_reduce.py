# map(), filter() and reduce() are also higher order functions in python

# map(func, iterable)
# map() function takes two arguments, first argument function and second an iterable
# It changes each element of the iterable to a new form as defined by the function
# Return of the map function is a map_object which is an iterator
# You can convert the iterator to any iterables (list, tuple, set) and loop upon it
# The number of elements in the initial iterable and the final result are same

data = [5, 4, 3, 2, 1]
result = []
for each in data:
    result.append(each * 5)
print(result)

result = [each * 5 for each in data]

print(result)  # [25, 20, 15, 10, 5]


def multiply_by_5(element):
    return element * 5


result = map(multiply_by_5, data)
print(result)  # map_object
print(list(result))



# filter(func, iterable)
# filter() function takes two arguments, first argument function and second an iterable
# It filters out elements of the iterable as defined by the function
# Return of the filter function is a filter object which is an iterator
# You can convert the iterator to any iterables (list, tuple, set) and loop upon it
# The number of elements in the initial iterable and the final result may or may not be same
# The function should return truthy or falsy statement


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [each for each in data if each % 2 == 0]

print(result)  # [2, 4, 6, 8, 10]


get_even = lambda element: element


result = filter(get_even, data)
print(result)
print(list(result))



# reduce(func, iterable)
# reduce() function takes two arguments, first argument function and second an iterable
# It calculate the elements of the iterable and return a single value as defined by the function
# Return of the reduce function is a single value / item
# The number of elements in the initial iterable and the final result is not same because reduce() returns a single value



data = [1, 2, 3, 4, 5]
from functools import reduce

multiply = lambda x, y: x * y

result = reduce(multiply, data)
print(result)  # 120