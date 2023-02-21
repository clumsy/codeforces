t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    a = [0] + a + [1440]
    res = sum((a[i + 1] - a[i]) // 120 for i in range(len(a) - 1))
    res = "YES" if res > 1 else "NO"
    print(res)
