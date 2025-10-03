t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    ma, dr = 0, False
    for i in a:
        dr = dr or i <= ma
        ma = max(ma, i)
    res = 1 if dr else n + 1 - ma
    print(res)
