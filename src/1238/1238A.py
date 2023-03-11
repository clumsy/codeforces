t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if x - y > 1 else "NO"
    print(res)
