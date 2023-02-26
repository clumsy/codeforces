t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    pwr = 0
    for i in range(n):
        while a[i] & 1 == 0:
            a[i] //= 2
            pwr += 1
    a.sort()
    a[-1] *= 2**pwr
    res = sum(a)
    print(res)
