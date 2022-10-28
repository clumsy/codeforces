t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    for _ in range(m):
        input()
    res = "YES" if m == 1 and n > 1 or m < n else "NO"
    print(res)
