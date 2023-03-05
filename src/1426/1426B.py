t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = "NO" if m & 1 == 1 else None
    for _ in range(n):
        tile = [[int(i) for i in input().split()] for _ in range(2)]
        if not res and tile[0][1] == tile[1][0]:
            res = "YES"
    res = res if res else "NO"
    print(res)
