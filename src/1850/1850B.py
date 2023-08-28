t = int(input())
for _ in range(t):
    n = int(input())
    max_b, res = -1, None
    for k in range(n):
        a, b = (int(i) for i in input().split())
        if a <= 10:
            if b > max_b:
                res, max_b = k + 1, b
    print(res)
