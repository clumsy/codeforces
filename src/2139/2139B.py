t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = sum(max(0, (m - n + 1 + i) * e) for i, e in enumerate(sorted(a)))
    print(res)
