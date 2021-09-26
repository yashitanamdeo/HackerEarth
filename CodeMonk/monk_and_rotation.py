T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A = list(input().split())
    index = N - (K%N)
    for i in range(index, N):
        print(A[i],end=" ")
    for i in range(index):
        print(A[i],end=" ")
    print("")