t = int(input())
for _ in range(t):
    n, p = int(input()), (int(i) for i in input().split())
    cnt = sum(i + 1 == e for i, e in enumerate(p))
    res = (cnt + 1) // 2
    print(res)
