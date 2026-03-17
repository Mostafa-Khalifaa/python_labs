num = int(input("Enter the number :"))

for i in range(num):
    lvl = ""
    for j in range(num):
        if i + j >= num - 1:
            lvl = lvl + "*"
        else:
            lvl = lvl + " "
    print(lvl)