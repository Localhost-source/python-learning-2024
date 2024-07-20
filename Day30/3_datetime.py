from datetime import datetime, timedelta


print(datetime.now())
data = datetime.now()

print(type(data))

data = str(datetime.now())
print(data)

today = datetime.now().year
print(type(today))
print(today)


data = "2024-07-01"
date_object = datetime.strptime(data, "%Y-%m-%d").date()
print(date_object)
print(type(date_object))


after_a_week = datetime.today() + timedelta(days=7)
print(after_a_week)
print(type(after_a_week))

# tkinter