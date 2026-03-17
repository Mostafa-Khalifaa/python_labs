

word = input("Enter a word: ")
res = ""
vowels = [ 'a', 'e', 'i', 'o', 'u']
for i in word:
    if i not in vowels:
        res += i

print(res)