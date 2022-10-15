t = int(input())
for _ in range(t):
    a, b, c = input(), input(), input()
    res = True
    for i in range(len(a)):
        res = a[i] == c[i] or b[i] == c[i]
        if not res:
            break
    res = "YES" if res else "NO"
    print(res)
