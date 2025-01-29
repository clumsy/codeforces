t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    res = "YES" if (a - b) & 1 == 0 else "NO"
    print(res)
