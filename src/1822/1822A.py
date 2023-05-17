q = int(input())
for _ in range(q):
    n, t = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = -2
    for i in range(n):
        if i + a[i] <= t and (res < 0 or b[res] < b[i]):
            res = i
    res += 1
    print(res)
