t = int(input())
for _ in range(t):
    x1, y1 = (int(i) for i in input().split())
    s1 = 1 if x1 > y1 else -1 if x1 < y1 else 0
    x2, y2 = (int(i) for i in input().split())
    s2 = 1 if x2 > y2 else -1 if x2 < y2 else 0
    res = "NO" if s1 != 0 and s2 != 0 and s1 != s2 else "YES"
    print(res)
