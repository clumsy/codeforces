q = int(input())
for _ in range(q):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = 1
    for i in range(1, n):
        if a[i] - a[i - 1] == 1:
            res = 2
            break
    print(res)
