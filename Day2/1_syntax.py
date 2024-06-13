# Identifiers
# Identifiers are the name provided by the programmer to variables, function and classes
# Keywords are the reserver words in a programming language

print(help("keywords"))

# Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

# Rules for naming identifiers
# 1. An identifier can't start with a number
a = 1  # here "a" is a valid identifier
print(a)
# 3b = 12  # here "3b" is an invalid identifier because it started with a number


# 2. Identifiers name are case-sensitive
A = [1, 2, 3]
a = 12
print(A) # [1, 2, 3]
print(a)  # 12

# 3. Keywords can't be used as an identifier name
# for = 12 # Invalid because "for" is a keyword


# 4. Identifier can contain underscore(_) at any place
_a = 1
__a__ = 2
_asdf_ = 12
_ = 12
___ = 13

# 5. It can't be started with a number but a number can occur at other places
# 1a = 12  # Invalid
a1 = 12  # Valid

# If you want to create a variable with multiple words then use snake case
StudentName = "Jon"  # Pascal Case variable
studentName = "Jon"  # Camel Case
student_name = "Jon"  # snake case variable

# But if you want to create class then use PascalCase
class Student:
    pass

class StudentInformation:
    pass

# But a better function name is snake case.