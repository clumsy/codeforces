t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    if n & 1 == 1:
        print("NO")
    else:
        res = "YES"
        a = [i for f, s in zip(a[: n // 2], a[n // 2 :]) for i in (f, s)]
        for i in range(1, n - 2, 2):
            if a[i] <= a[i - 1] or a[i + 1] >= a[i] or a[i + 1] >= a[i + 2]:
                res = "NO"
                break
        print(res)
        if res == "YES":
            print(*a)
