t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = 0 if n == m == 1 else min(n, m, 2)
    print(res)
