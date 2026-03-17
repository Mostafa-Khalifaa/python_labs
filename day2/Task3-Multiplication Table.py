
num = int(input("Enter a number: "))
list = []
for i in range(1,num+1):
    list2 = []
    for j in range(1,i+1):
        list2.append(i*j)
    list.append(list2)
print(list)
