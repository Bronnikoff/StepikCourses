code = input().lower()
key = input().lower()

alfa = "abcdefghijklmnopqrstuvwxyz"

tabl = {}

for i in range(len(key)):
    tabl[key[i]] = alfa[i]

for i in code:
    if i >= 'a' and i <= 'z':
        print(tabl[i], end = "")
    else:
        print(i, end = "")

print()