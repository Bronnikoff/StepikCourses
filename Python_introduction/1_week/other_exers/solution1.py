string1 = input()
string2 = input()

string1 = string1.lower()
string2 = string2.lower()

diction = {}

for i in string2:
    if i <= 'z' and i >= 'a':
        diction[i] = []

for i in range(len(string1)):
    if diction.get(string1[i]) != None:
        diction[string1[i]].append(i)

for i in diction:
    print(i, end = "")
    if diction[i] != []: 
        for j in diction[i]:
            print("", j+1, end = "")
        print("")
    else:
        print(" None")
    