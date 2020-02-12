from random import randint

N = int(input())
inp = input().split()

lim = int(inp[0])
seria = inp[1].upper()

if N >= lim:
    for i in range(1, lim + 1):
        print("Победитель номер", i + 1, end = "")
        print(r' - "', end = "")
        print("%.6d" % (i), seria, end = "")
        print(r'"')

else:
    l = []
    for i in range(N):
        num = randint(1, lim)
        while l.count(num) != 0:
            num = randint(1, lim)
        l.append(num)
        print("Победитель номер", i + 1, end = "")
        print(r' - "', end = "")
        print("%.6d" % (num), seria, end = "")
        print(r'"')

