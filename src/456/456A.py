n = int(input())
ltps = [[int(i) for i in input().split()] for _ in range(n)]
ltps.sort()
res, ma = "Poor Alex", 0
for i in range(n):
    if ltps[i][0] > ltps[ma][0] and ltps[i][1] < ltps[ma][1]:
        res = "Happy Alex"
        break
    if ltps[i][1] > ltps[ma][1]:
        ma = i
print(res)
