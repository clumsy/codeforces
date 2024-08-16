t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    if a & 1 == 1 or (b & 1 == 1 and a == 0):
        res = "NO"
    else:
        res = "YES"
    print(res)
