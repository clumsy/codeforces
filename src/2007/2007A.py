t = int(input())
for _ in range(t):
    l, r = (int(i) for i in input().split())
    e = (r - l + 1) // 2 + (r & 1 == l & 1 == 0)
    o = r - l + 1 - e
    res = min(e, o // 2)
    print(res)
