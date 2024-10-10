t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    m1, m2 = a[0], None
    res = "YES"
    for i in a:
        if i % m1 == 0:
            continue
        if m2 is None:
            m2 = i
        elif i % m2 != 0:
            res = "NO"
            break
    print(res)
