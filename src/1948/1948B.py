t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    prv = a[-1]
    res = "YES"
    for i in reversed(range(n - 1)):
        if a[i] > prv:
            for d in str(a[i])[::-1]:
                d = int(d)
                if d <= prv:
                    prv = d
                else:
                    res = "NO"
                    break
        else:
            prv = a[i]
        if res == "NO":
            break
    print(res)
