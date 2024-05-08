t = int(input())
for _ in range(t):
    a, b, n = (int(i) for i in input().split())
    x = sorted(int(i) for i in input().split())
    res = 0
    for i in x:
        if b + i > a:
            res += b - 1
            b = min(i + 1, a)
        else:
            b += i
    res += b
    print(res)
