t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    i, c = 1, 0
    while i < n:
        if a[i - 1] > a[i]:
            c += 1
            i += 1
        i += 1
    print(c)
