t = int(input())
for _ in range(t):
    c = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    for i in range(3):
        cnt = min(c[i], a[i])
        c[i] -= cnt
        a[i] -= cnt
    for i in range(2):
        cnt = min(c[i], a[3 + i])
        c[i] -= cnt
        a[3 + i] -= cnt
    for i in range(2):
        cnt = min(c[2], a[3 + i])
        c[2] -= cnt
        a[3 + i] -= cnt
    res = "YES" if all(i == 0 for i in a) else "NO"
    print(res)
