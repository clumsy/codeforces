n, a, b = (int(i) for i in input().split())
if n > a * b:
    print(-1)
else:
    res = [[0] * b for _ in range(a)]
    for r in range(a):
        for c in range(b):
            x = r * b + c + 1
            if x > n:
                break
            res[r][c if r & 1 == 0 else b - 1 - c] = x
        if x > n:
            break
    for r in res:
        print(*r)
