# Using context manager we donot need to manually close a file

with open("example.txt", "r") as fp:
    data = fp.read()
    print(data)


with open("example.txt", "w") as fp:
    fp.write("Using context Manager")
print("Written to file")


with open("example.txt", "a") as fp:
    fp.write("\nThis is in new line")

with open("example.txt", "r+") as fp:
    data = fp.read()
    print(data)
    fp.seek(0)
    fp.write("New Data")

with open("example.txt", "w+") as fp:
    fp.write("Completely new data")
    fp.seek(0)
    data = fp.read()
    print(data, "<--------")


# File can be opened in exclusive mode if it doesnt exist. If it exists then it raises error.
with open("example1.txt", "x") as fp:
    fp.write("Exclusively")