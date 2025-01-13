t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = max(m, n) + 1
    print(res)
