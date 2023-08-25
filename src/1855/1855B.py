t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        if n % i != 0:
            break
        res += 1
    print(res)
