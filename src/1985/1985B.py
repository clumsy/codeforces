t = int(input())
for _ in range(t):
    n = int(input())
    # x(1 + ... + k) = n => x(1 + k)k/2 = n
    ma = 0
    for i in range(2, n + 1):
        k = n // i
        s = i * (1 + k) * k // 2
        if s > ma:
            ma, x = s, i
    res = x
    print(res)
