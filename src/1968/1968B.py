t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a, b = (input() for _ in range(2))
    res = 0
    for c in b:
        res += c == a[res]
        if res == n:
            break
    print(res)
