t = int(input())
for _ in range(t):
    r, b, d = (int(i) for i in input().split())
    r, b = min(r, b), max(r, b)
    res = "YES" if r <= b <= r + d * r else "NO"
    print(res)
