t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    k = gap = 0
    res = "YES"
    for i in range(n):
        if a[i] > b[i]:
            res = "NO"
            break
        if gap != 0:
            if b[i] == a[i]:
                gap = 0
            elif b[i] - a[i] != gap:
                res = "NO"
                break
        elif gap == 0:
            gap = b[i] - a[i]
            k += gap > 0
        if k > 1:
            res = "NO"
            break
    print(res)
