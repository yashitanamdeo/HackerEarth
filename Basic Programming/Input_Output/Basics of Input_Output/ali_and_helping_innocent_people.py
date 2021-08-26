s = input()

valid = False

vowels = ["A","E","I","O","U","Y"]

if ((int(s[0]) + int(s[1])) % 2 == 0) and (s[2] not in vowels) and ((int(s[3]) + int(s[4])) % 2 == 0) and ((int(s[4]) + int(s[5])) % 2 == 0) and ((int(s[7]) + int(s[8])) % 2 == 0):
    valid = True

if valid:
    print("valid")
else:
    print("invalid")