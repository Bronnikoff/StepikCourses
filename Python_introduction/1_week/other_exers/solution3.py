k = int(input())

res = 0

for i in range(k):
    inp = input().split()
    x = float(inp[0])
    y = float(inp[1])
    r = int((x**2 + y**2)**0.5)
    if r < 10:
        res += (10 - r)

print(res)
