
word = input("Enter a word: ")
letter = input("Enter a letter: ")
list = []
for i in range(len(word)):
    if word[i] == letter:
        list.append(i)
print(list)
