def fence(string):
    res=""
    if "HH" in string:
        return "NO"
    else:
        res = string.replace(".","B")
    return "YES"+"\n"+res
 
 
n = int(input())
string = input()
print(fence(string))