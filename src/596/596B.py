n = int(input())
b = (int(i) for i in input().split())
res = prv = 0
for i in b:
    res += abs(i - prv)
    prv = i
print(res)
