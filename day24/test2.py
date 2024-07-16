import sys
import os

# Add the directory containing day1 to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'day1')))

from test1 import addition, A
from day1 import operators
from day1 import operators as op
from day1.operators import a


result = addition(4, 5)
print(result)
print(A)

print(operators.a)
print(op.a)
print(a)
