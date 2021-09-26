S = input()
S.split()
for i in S:
    if i.islower():
        S = i.upper()
    else:
        S = i.lower()
    print(S,end="")