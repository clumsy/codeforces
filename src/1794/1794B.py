t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    for i in range(n):
        if a[i] == 1:
            a[i] += 1
        if i > 0 and a[i] % a[i - 1] == 0:
            a[i] += 1  # e.g. same parity
    res = a
    print(*res)
