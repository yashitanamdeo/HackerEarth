n = int(input())
integers = list(map(int,input().split()))
integerList = []
count = 0

for integer in integers:
    if integer not in integerList:
        integerList.append(integer)
        count += 1
    
print(count)