n = int(input())
for _ in range(n):
    x, y = (int(i) for i in input().split())
    y -= abs(x) - 1
    res = "YES" if y >= -abs(x) else "NO"
    print(res)
