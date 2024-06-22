import string


t = int(input())
for _ in range(t):
    n, a = int(input()), input()
    s = next((i for i in range(n) if a[i] in string.ascii_lowercase), n)
    d, c = a[:s], a[s:]
    res = "YES"
    for i in range(1, len(c)):
        if c[i] < c[i - 1]:
            res = "NO"
    for i in range(1, len(d)):
        if d[i] < d[i - 1]:
            res = "NO"
    print(res)
