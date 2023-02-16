t = int(input())
for _ in range(t):
    n = int(input())
    res = [0] * n
    res[n - 2 :] = n - 1, n
    if n & 1 == 1:
        res[0] = 1
    for i in range(n & 1, n - 2):
        res[i] = n - 2 - i + (n & 1)
    print(*res)
