t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    m, b = 0, 0
    for i in a:
        m += i if i & 1 == 0 else 0
        b += i if i & 1 != 0 else 0
    res = "YES" if m > b else "NO"
    print(res)
