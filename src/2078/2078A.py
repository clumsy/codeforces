t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = "YES" if sum(a) / n == x else "NO"
    print(res)
