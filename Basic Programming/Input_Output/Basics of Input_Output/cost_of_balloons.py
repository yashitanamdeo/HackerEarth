T = int(input())

for _ in range(T):
    costGreen, costPurple = map(int,input().split())
    n = int(input())
    sum1,sum2 = 0,0
    for i in range(n):
        userI,userJ = map(int,input().split())

        sum1 = (userI * costGreen + userJ * costPurple) + sum1 
        sum2 = (userI * costPurple + userJ * costGreen) + sum2

    print(min(sum1,sum2))