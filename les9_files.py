# file = open("test_file3", "w", encoding="UTF-8")
# # file.write("hello")
# print("HELLO WORLD", file=file, end="########")
# # print(result)
import random


user_names = ["Gauss", "Bill", "Illon", "R2D2"]
homes = ["Berlin", "Los-Angeles", "Death Star"]

users = [
    {
        "name": random.choice(user_names),
        "age": random.randint(30, 80),
        "home": random.choice(homes),
    }
    for _ in range(20)
]
file = open("users", "w", encoding="UTF-8")
delim = ","
try:
    for idx, itm in enumerate(users):
        if not idx:
            file.write(f"{delim.join(itm.keys())}\n")
        file.write(f"{delim.join(map(str, itm.values()))}\n")
except FileNotFoundError as e:
    pass
finally:
    file.close()

result = []
keys = []
file = open("users", "r", encoding="UTF-8")
for idx, line in enumerate(file):
    if not idx:
        keys = line.split(delim)
    else:
        values = line.split(delim)
        result.append(dict(zip(keys, values)))
print(1)
# file = open("test_file", "r")
# try:
#     file.seek(0, 2)
#     data = file.read()
#     print(file.tell())
# except Exception as exc:
#     pass
# finally:
#     file.close()
