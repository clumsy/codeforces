t = int(input())
for _ in range(t):
    x, y, a = (int(i) for i in input().split())
    a = a % (x + y)
    a += 0.5
    res = "NO" if a <= x else "YES"
    print(res)
