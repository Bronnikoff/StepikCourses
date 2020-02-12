import sys
num_steps = int(sys.argv[1])

num_steps += 1

for i in range(1, num_steps):
    for j in range(1, num_steps - i):
        print(' ', end = "")
    for j in range(num_steps-i, num_steps):
        print('#', end = "")
    print("")

