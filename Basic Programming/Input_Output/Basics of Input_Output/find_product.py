M = (10**9)+7
product = 1
N = int(input())
elements = list(map(int,input().split()))
for i in elements:
    product = (product * i) % M
print(product) 