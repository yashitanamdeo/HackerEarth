N = int(input())
A = list(input().split())
num = []
for i in range(N//2): #first half
    num.append(int(A[i][0]))
for j in range(N//2,N): #second half
    num.append(int(A[j][-1]))

# list to int conversion
strings = [str(num1) for num1 in num]
string = "". join(strings)
number = int(string)

# testing if newly-generated number is divisible by 11
if number % 11 == 0:
    print("OUI")
else:
    print("NON")