import sys

digit_string = sys.argv[1]

res = 0

for i in digit_string:
    res += int(i)

print(res)