t = int(input())
for _ in range(t):
    n, d = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    res = "YES" if a[-1] <= d or sum(a[:2]) <= d else "NO"
    print(res)
