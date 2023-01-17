t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = "YES" if sum(a) == m else "NO"
    print(res)
