names = ["mostafa","Khalifa", "Mohsen", "ahmed","Nader", "ali","khalid"]
res = {}

for name in names:
    key = name[0].lower()
    if key not in res:
        res[key] = []
    res[key].append(name)

print(res)