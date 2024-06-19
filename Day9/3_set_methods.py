# union()
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s = s1.union(s2)
print(s)  # {1, 2, 3, 4, 5, 6}

s = s1 | s2
print(s)  # {1, 2, 3, 4, 5, 6}


# intersection()
s = s1.intersection(s2)
print(s)  # {3, 4}  
s = s1 & s2  
print(s)  # {3, 4}

s1.intersection_update(s2)
print(s1)  # {3, 4}


# difference
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s = s1.difference(s2)
print(s)  # {1, 2}

s = s1 - s2
print(s)  # {1, 2}

s = s2.difference(s1)
print(s)  # {5, 6}

s1.difference_update(s2)
print(s1)  # {1, 2}


# symmetric_difference
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s = s1.symmetric_difference(s2)
print(s)  # {1, 2, 5, 6}

s = s1 ^ s2
print(s)  # {1, 2, 5, 6}

s1.symmetric_difference_update(s2)
print(s1)  # {1, 2, 5, 6}