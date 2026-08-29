from datetime import datetime
a = datetime.now()
b = datetime(2020, 1, 1)

print(type(a))
print(a - b)
print((a - b).days)