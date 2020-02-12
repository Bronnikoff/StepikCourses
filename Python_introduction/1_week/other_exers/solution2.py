string = input()

string = string.lower()

l = []

for i in string:
    if i >= 'a' and i <= 'z' and l.count(i) == 0:
        l.append(i)

l.sort()

for i in l:
    print(i, end = "")
print()
        