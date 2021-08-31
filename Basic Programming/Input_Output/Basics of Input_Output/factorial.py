N = int(input())
fact = 1
for i in range(1,N+2):
    if i<=N:
        fact *= i
print(fact)