# Exception handling is done using try...except block in Python


# 1. try....except
try:
    data = int(input("Enter a number "))
    
except:
    print("Please provide a valid integer")


# 2. try...except ErrorTYpe
try:
    data = int(input("Enter a number "))
except ValueError:
    print("Please provide a valid integer")
    
# 3. try...except...except...
try:
    data = int(input("Enter a number "))
except ValueError:
    print("Please provide a valid integer")
except TypeError:
    print("Please check your operations and operators")
    
    
# 4. try...except (MultipleErrors...)
try:
    data = int(input("Enter a number "))
except (ValueError, IndexError, TypeError):
    print("Something Went Wrong")


# 5. try...except...else
try:
    data = int(input("Enter a number "))
except:
    print("Something Went Wrong")
else:
    a = 1
    b = 2
    print(data + a + b)
    
    
# 6. try...except...finally
try:
    data = int(input("Enter a number "))
except:
    print("Something Went Wrong")
else:
    a = 1
    b = 2
    print(data + a + b)
finally:
    print("This is always executed")