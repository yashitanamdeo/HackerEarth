word = input()
countZ,countO = 0, 0
for i in range(len(word)):
    if word[i] == 'z':
        countZ += 1
    else:
        countO += 1
if 2 * countZ == countO:
    print("Yes")
else:
    print("No")