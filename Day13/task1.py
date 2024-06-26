# Create a student dictionary. 
# Create a function which takes dictionary key (string) as argument and return the value of that key


student = {"name": "Alex", "age": 30, "address": "KTM"}

def get_value(key):
    return student.get(key, "Key not found")

key = input("Enter the key you want to access: ")
result = get_value(key)
print(result)