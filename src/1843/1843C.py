t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    while n:
        res += n
        n //= 2
    print(res)
